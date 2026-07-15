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

// Honeypot: real users never fill this hidden field.
if (field('company') !== '') {
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

$errors = [];
if ($pickup === '' || $dropoff === '') $errors[] = 'pickup and destination';
if ($name === '') $errors[] = 'your name';
if ($email === '' || !filter_var($email, FILTER_VALIDATE_EMAIL)) $errors[] = 'a valid email';
if ($pickupDate === '') $errors[] = 'pickup date';
if ($pickupTime === '') $errors[] = 'pickup time';
if ($phone === '') $errors[] = 'a phone number';
if ($flight === '') $errors[] = 'pickup details';

if ($errors) {
    http_response_code(400);
    echo json_encode(['success' => false, 'error' => 'Please provide ' . implode(', ', $errors) . '.']);
    exit;
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
          customer_name, customer_email, customer_phone, flight, dropoff_details, notes)
         VALUES
         (NOW(), :pickup, :dropoff, :trip, :pdate, :ptime,
          :rdate, :rtime, :pax, :lug, :price,
          :name, :email, :phone, :flight, :dropoff_details, :notes)'
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
$lines[] = 'Quoted price: ' . ($price !== '' ? '€' . $price : 'custom');
$lines[] = "Name: {$name}";
$lines[] = "Email: {$email}";
$lines[] = 'Phone: ' . ($phone !== '' ? $phone : 'not provided');
if ($flight !== '') $lines[] = "Pickup details: {$flight}";
if ($dropoffDet !== '') $lines[] = "Destination details: {$dropoffDet}";
if ($notes !== '') $lines[] = "Notes: {$notes}";
$summary = implode("\n", $lines);

$c = tx_config();
$headers = 'From: TAXI Antonio <' . $c['mail_from'] . ">\r\n" .
           'Reply-To: ' . $email . "\r\n" .
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
    . '<p>Thank you for your booking request. I have received it and will get back to you as soon as I am available.</p>'
    . '<p><strong>Your request:</strong><br>' . $custSummaryHtml . '</p>'
    . '<p>If anything is wrong, just reply to this email.</p>'
    . '<p>Best regards,<br>Antonio Šakić</p>'
    . $sig
    . '</div>';
$custHeaders = 'From: TAXI Antonio <' . $c['mail_from'] . ">\r\n" .
               'Reply-To: ' . $c['admin_email'] . "\r\n" .
               "MIME-Version: 1.0\r\n" .
               "Content-Type: text/html; charset=utf-8\r\n";
@mail($email, 'Booking request received', $custBody, $custHeaders);

echo json_encode(['success' => true, 'id' => $id]);
