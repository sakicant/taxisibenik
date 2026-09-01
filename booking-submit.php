<?php
/**
 * Public endpoint that receives a booking from the /book/ page,
 * stores it in the database, and emails Antonio + the customer.
 * Returns JSON so the existing front-end fetch() keeps working.
 */

require __DIR__ . '/db.php';

header('Content-Type: application/json');

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'error' => 'Method not allowed']);
    exit;
}

// Throttle abuse: at most 6 booking submissions per IP per hour.
if (!tx_rate_limit('booking', 6, 3600)) {
    http_response_code(429);
    echo json_encode(['success' => false, 'error' => 'Too many requests. Please try again shortly, or call/WhatsApp me.']);
    exit;
}

function field($key, $max = 255)
{
    $v = isset($_POST[$key]) ? trim((string) $_POST[$key]) : '';
    $v = str_replace(["\r", "\n", "\0"], ' ', $v);
    return mb_substr($v, 0, $max);
}

// Authoritative fare lookup. prices.json is generated from the PRICES matrix
// in script.js at build time, so the server never trusts the ?price= value
// that came in through the booking URL (which a visitor could edit).
function tx_prices()
{
    static $PRICES = null;
    if ($PRICES === null) {
        $p = @file_get_contents(__DIR__ . '/prices.json');
        $PRICES = $p ? (json_decode($p, true) ?: []) : [];
    }
    return $PRICES;
}

// Lowercase, strip diacritics and punctuation, collapse spaces: "Split airport"
// and "Split Airport (SPU)" both normalise onto comparable strings.
function tx_norm($s)
{
    $s = mb_strtolower(trim((string) $s), 'UTF-8');
    $s = strtr($s, ['š' => 's', 'đ' => 'd', 'č' => 'c', 'ć' => 'c', 'ž' => 'z']);
    $s = preg_replace('/[^a-z0-9]+/u', ' ', $s);
    return trim(preg_replace('/\s+/', ' ', $s));
}

// Resolve what the visitor typed to a canonical PRICES place name. Customers
// often type "skradin" or "split airport" by hand; exact matching alone made
// most bookings fall through to "custom". A fuzzy match is only accepted when
// it is unambiguous (exactly one candidate), so nobody gets the wrong fare.
function tx_resolve_place($input)
{
    static $index = null;
    if ($index === null) {
        $index = [];
        $prices = tx_prices();
        $keys = array_keys($prices);
        foreach ($prices as $sub) {
            foreach (array_keys($sub) as $k) $keys[] = $k;
        }
        foreach (array_unique($keys) as $k) $index[tx_norm($k)] = $k;
    }
    $n = tx_norm($input);
    if ($n === '') return null;
    if (isset($index[$n])) return $index[$n];         // exact (normalised)
    if (isset($index[$n . ' center'])) return $index[$n . ' center'];   // "sibenik" -> "Sibenik - center"
    $starts = [];
    $within = [];
    foreach ($index as $nk => $k) {
        if (strpos($nk, $n) === 0) $starts[$k] = true;          // "split airport" -> "split airport spu"
        elseif (strpos($n, $nk) === 0) $within[$k] = true;      // "sibenik bus station main" -> "sibenik bus station"
    }
    if (count($starts) === 1) return array_key_first($starts);
    if (count($starts) === 0 && count($within) === 1) return array_key_first($within);
    return null;                                       // ambiguous or unknown
}

function tx_price_oneway($from, $to)
{
    $PRICES = tx_prices();
    if (isset($PRICES[$from][$to])) return $PRICES[$from][$to];
    if (isset($PRICES[$to][$from])) return $PRICES[$to][$from];
    $f = tx_resolve_place($from);
    $t = tx_resolve_place($to);
    if ($f === null || $t === null) return null;
    if (isset($PRICES[$f][$t])) return $PRICES[$f][$t];
    if (isset($PRICES[$t][$f])) return $PRICES[$t][$f];
    return null;
}

// Honeypot: real users never see this hidden field, but form-spam bots fill it
// with links. Only reject on link-like content, so a browser or password
// manager auto-filling the hidden "company" field can't silently drop a real
// booking (an autofilled company name has no URL and passes through).
if (preg_match('#https?://|www\.#i', field('company'))) {
    echo json_encode(['success' => true]);
    exit;
}

$pickup      = field('pickup', 120);
$dropoff     = field('dropoff', 120);
$trip        = field('trip', 20) === 'return' ? 'return' : 'oneway';
$pickupDate  = field('pickup_date', 20);
$pickupTime  = field('pickup_time', 20);
$returnDate  = field('return_date', 20);
$returnTime  = field('return_time', 20);
$passengers  = (int) field('passengers', 3);
$luggage     = (int) field('luggage', 3);
$price       = field('price', 40);
$name        = field('name', 120);
$email       = field('email', 160);
$phone       = field('phone', 60);
$flight      = field('flight', 120);
$dropoffDet  = field('dropoff_details', 120);
$notes       = isset($_POST['notes']) ? mb_substr(trim((string) $_POST['notes']), 0, 2000) : '';

// Preferred contact method + payment choice + company-invoice flag (new form).
$contactMethod = field('contact_method', 20);
$paymentOption = field('payment_option', 20);
$invoiceReq    = !empty($_POST['invoice_required']) ? 1 : 0;
if ($contactMethod !== 'whatsapp' && $contactMethod !== 'email') $contactMethod = '';
// Deposit is the only payment option offered; paying in full up front was removed.
if ($paymentOption !== 'deposit') $paymentOption = '';

// Company invoice details, only sent when the visitor ticks the invoice box.
$coName    = $invoiceReq ? field('company_name', 160) : '';
$coVat     = $invoiceReq ? field('company_vat', 40) : '';
$coAddress = $invoiceReq ? field('company_address', 160) : '';
$coZip     = $invoiceReq ? field('company_zip', 20) : '';
$coCity    = $invoiceReq ? field('company_city', 80) : '';

$errors = [];
if ($pickup === '' || $dropoff === '') $errors[] = 'pickup and destination';
if ($name === '') $errors[] = 'your name';
// Contact requirement honours the chosen method. WhatsApp-only bookings do not
// need an email; if one is given it must still be valid. A form with no method
// chooser (legacy) keeps the original "email required" rule.
if ($contactMethod === 'whatsapp') {
    if ($phone === '') $errors[] = 'your WhatsApp number';
    if ($email !== '' && !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'a valid email';
} else {
    if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'a valid email';
}
if ($flight === '') $errors[] = 'pickup details (flight number or address)';
if ($pickupDate === '') $errors[] = 'pickup date';
if ($pickupTime === '') $errors[] = 'pickup time';

if ($errors) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Please provide ' . implode(', ', $errors) . '.']);
    exit;
}

// Recompute the fixed fare from the route itself, ignoring the submitted
// price, so editing ?price= in the booking link cannot change what is stored.
if ($passengers >= 5) {
    $price = 'custom';                       // van needed, quoted by hand
} elseif (tx_norm($pickup) === tx_norm($dropoff)) {
    $price = 'meter';                        // local ride, on the taxi meter
} else {
    $ow = tx_price_oneway($pickup, $dropoff);
    if ($ow === null) {
        $price = 'custom';                   // no fixed fare for this route
    } else {
        $price = (string) ($trip === 'return' ? $ow * 2 : $ow);
    }
}

$passengers = max(1, min(4, $passengers));
$luggage    = max(0, min(9, $luggage));

// Normalise date/time to NULL when empty so MySQL accepts them.
$nn = function ($v) { return $v === '' ? null : $v; };

try {
    $stmt = tx_db()->prepare(
        'INSERT INTO bookings
         (created_at, pickup, dropoff, trip_type, pickup_date, pickup_time,
          return_date, return_time, passengers, luggage, quoted_price,
          customer_name, customer_email, customer_phone, flight, dropoff_details, notes,
          contact_method, payment_option, invoice_required,
          company_name, company_vat, company_address, company_zip, company_city)
         VALUES
         (NOW(), :pickup, :dropoff, :trip, :pdate, :ptime,
          :rdate, :rtime, :pax, :lug, :price,
          :name, :email, :phone, :flight, :dropoff_details, :notes,
          :contact_method, :payment_option, :invoice_required,
          :company_name, :company_vat, :company_address, :company_zip, :company_city)'
    );
    $stmt->execute([
        ':pickup' => $pickup,
        ':dropoff' => $dropoff,
        ':trip' => $trip,
        ':pdate' => $nn($pickupDate),
        ':ptime' => $nn($pickupTime),
        ':rdate' => $nn($returnDate),
        ':rtime' => $nn($returnTime),
        ':pax' => $passengers,
        ':lug' => $luggage,
        ':price' => $nn($price),
        ':name' => $name,
        ':email' => $email,
        ':phone' => $nn($phone),
        ':flight' => $nn($flight),
        ':dropoff_details' => $nn($dropoffDet),
        ':notes' => $notes === '' ? null : $notes,
        ':contact_method' => $nn($contactMethod),
        ':payment_option' => $nn($paymentOption),
        ':invoice_required' => $invoiceReq,
        ':company_name' => $nn($coName),
        ':company_vat' => $nn($coVat),
        ':company_address' => $nn($coAddress),
        ':company_zip' => $nn($coZip),
        ':company_city' => $nn($coCity),
    ]);
    $id = tx_db()->lastInsertId();
} catch (PDOException $e) {
    http_response_code(500);
    error_log('Booking insert failed: ' . $e->getMessage());
    echo json_encode(['success' => false, 'error' => 'Could not save your booking. Please call or WhatsApp me instead.']);
    exit;
}

// Build a readable summary for the emails.
$lines = [
    "Route: {$pickup} -> {$dropoff}",
    'Trip: ' . ($trip === 'return' ? 'Return' : 'One way'),
    "Pickup: {$pickupDate} {$pickupTime}",
];
if ($trip === 'return') {
    $lines[] = 'Return: ' . ($returnDate !== '' ? $returnDate : 'not set') . ' ' . $returnTime;
}
$lines[] = "Passengers: {$passengers}   Luggage: {$luggage}";
if (is_numeric($price)) {
    $priceLabel = 'EUR ' . $price . ($trip === 'return' ? ' (return total)' : ' (one way)');
} elseif ($price === 'meter') {
    $priceLabel = 'Taxi meter (local ride, from EUR 10)';
} else {
    $priceLabel = 'To be confirmed by Antonio (no fixed fare listed for this route)';
}
$lines[] = 'Price: ' . $priceLabel;
$lines[] = "Name: {$name}";
$lines[] = 'Email: ' . ($email !== '' ? $email : 'not provided');
$lines[] = 'Phone: ' . ($phone !== '' ? $phone : 'not provided');
if ($contactMethod !== '') {
    $lines[] = 'Preferred contact: ' . ($contactMethod === 'whatsapp' ? 'WhatsApp' : 'Email');
}
if ($paymentOption !== '') {
    $lines[] = 'Payment: deposit to confirm (20%, min EUR 20)';
}
if ($invoiceReq) {
    $lines[] = 'Company invoice: requested';
    if ($coName !== '')    $lines[] = "  Company: {$coName}";
    if ($coVat !== '')     $lines[] = "  VAT ID: {$coVat}";
    if ($coAddress !== '') $lines[] = "  Address: {$coAddress}";
    if ($coZip !== '' || $coCity !== '') $lines[] = trim("  {$coZip} {$coCity}");
}
if ($flight !== '') $lines[] = "Pickup details: {$flight}";
if ($dropoffDet !== '') $lines[] = "Destination details: {$dropoffDet}";
if ($notes !== '') $lines[] = "Notes: {$notes}";
$summary = implode("\n", $lines);

$c = tx_config();
$headers = 'From: TAXI Antonio <' . $c['mail_from'] . ">\r\n" .
           ($email !== '' ? 'Reply-To: ' . $email . "\r\n" : '') .
           "Content-Type: text/plain; charset=utf-8\r\n";

// Notify Antonio. The host tells us which site the booking came from.
$host = $_SERVER['HTTP_HOST'] ?? 'taxisibenik.hr';
$host = preg_replace('/^www\./i', '', preg_replace('/[^a-z0-9.\-]/i', '', $host));
@mail(
    $c['admin_email'],
    'New Booking Request (' . $host . ')',
    "New booking request (#{$id}) from {$host}:\n\n{$summary}\n\nManage it in the admin dashboard.",
    $headers
);

// Acknowledge the customer (HTML email with signature).
$sig = <<<'SIG'
<table style="padding-bottom:10px;margin-bottom:8px" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td><table style="display: inline-flex; margin-bottom: 30px;" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style="vertical-align: top;"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td><img src="https://cdn.trustindex.io/companies/ea/ea559b351365g599/media/whatsapp-image-2026-07-04-at-11-31.44.png" alt="Antonio Šakić" style="vertical-align:initial; max-width:80px;" width="80" height="80"></td></tr></tbody></table></td><td style="padding-left: 14px; "></td><td style="border-left: 2px solid #ccc; padding-right: 14px; "></td><td style="vertical-align: top;"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td><table style="line-height: 1.5em; font-family: sans-serif; font-size: 14px; color: #000000; font-weight: normal; width: 100%;" width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 14px; font-weight: bold; line-height: 1.5em;">Antonio Šakić</span><br><span style="color: rgb(0, 0, 0); font-family: sans-serif; font-size: 13px; line-height: 1.5em;">Owner</span></td></tr></tbody></table></td></tr><tr><td><table style="line-height: 1.5em;  font-family: sans-serif; font-size: 14px; color: #000000;  font-weight: normal; width: 100%;" width="100%" cellspacing="0" cellpadding="0" border="0"><tbody><tr><td style=" font-family: sans-serif; font-size:14px; color: #000000 !important;"><div style="font-family: sans-serif; font-size:14px; line-height: 1.5em; "><span style="padding: 0px; margin: 0px; color: rgb(0, 0, 0); font-family: sans-serif; font-weight: bold; font-size: 13px; line-height: 1.5em;">Mobile:</span> <span style="font-size: 13px;"><a style="text-decoration: none !important;  font-family: sans-serif; font-size:14px !important;  color: #000 !important; line-height: 1.5em; " href="tel:+385994471013"><span style="font-size: 13px;">+385994471013</span></a></span></div><div style="font-family: sans-serif; font-size:14px; line-height: 1.5em; "><span style="padding: 0px; margin: 0px; color: rgb(0, 0, 0); font-family: sans-serif; font-weight: bold; font-size: 13px; line-height: 1.5em;">Email:</span> <span style="font-size: 13px;"><a style="text-decoration: none !important;  font-family: sans-serif; font-size:14px !important;  color: #000 !important; line-height: 1.5em; " href="mailto:info@taxisibenik.hr"><span style="font-size: 13px;">info@taxisibenik.hr</span></a></span></div><div style="font-family: sans-serif; font-size:14px; line-height: 1.5em; "><span style="padding: 0px; margin: 0px; color: rgb(0, 0, 0); font-family: sans-serif; font-weight: bold; font-size: 13px; line-height: 1.5em;">Websites:</span> <span style="font-size: 13px;"><a style="text-decoration: none !important;  font-family: sans-serif; font-size:14px !important;  color: #000 !important; line-height: 1.5em; " href="https://taxisibenik.hr" target="_blank"><span style="font-size: 13px;">taxisibenik.hr</span></a> <span style="font-size: 13px;">and</span> <a style="text-decoration: none !important;  font-family: sans-serif; font-size:14px !important;  color: #000 !important; line-height: 1.5em; " href="https://taxiskradin.hr" target="_blank"><span style="font-size: 13px;">taxiskradin.hr</span></a></span></div></td></tr><tr><td><span style="padding-top: 15px;"></span></td></tr><tr><td style="padding-top: 12px;"><a href="https://admin.trustindex.io/widget/logClick?pub_widget_id=fbb695575514826d1b562e60499" target="_blank" style="text-decoration: none !important;"><table cellspacing="0" cellpadding="0" border="0"><tbody><tr><td><img alt="Rating stars" src="https://cdn.trustindex.io/widgets/fb/fbb695575514826d1b562e60499/stars.gif" style="display: block;"></td></tr><tr><td><img alt="Rating text" src="https://cdn.trustindex.io/widgets/fb/fbb695575514826d1b562e60499/text.gif" style="display: block;" width="122" height="15"></td></tr></tbody></table></a></td></tr></tbody></table></td></tr></tbody></table></td></tr><tr><td></td></tr></tbody></table>
SIG;
$custSummaryHtml = nl2br(htmlspecialchars($summary, ENT_QUOTES, 'UTF-8'));
$custBody = '<div style="font-family:sans-serif;font-size:14px;color:#000;line-height:1.6">'
    . '<p>Hi ' . htmlspecialchars($name, ENT_QUOTES, 'UTF-8') . ',</p>'
    . '<p>Thank you for your booking request. I have received it and will email you soon to confirm availability and send instructions for the advance payment that fully confirms your reservation.</p>'
    . '<p><strong>Your request:</strong><br>' . $custSummaryHtml . '</p>'
    . '<p>If anything is wrong, just reply to this email.</p>'
    . '<p>Best regards,<br>Antonio Šakić</p>'
    . $sig
    . '</div>';
$custHeaders = 'From: TAXI Antonio <' . $c['mail_from'] . ">\r\n" .
               'Reply-To: ' . $c['admin_email'] . "\r\n" .
               "MIME-Version: 1.0\r\n" .
               "Content-Type: text/html; charset=utf-8\r\n";
// Only email the customer when they left an address; WhatsApp-only bookings
// are confirmed by Antonio over WhatsApp instead.
if ($email !== '') {
    @mail($email, 'Booking request received', $custBody, $custHeaders);
}

echo json_encode(['success' => true, 'id' => $id]);
