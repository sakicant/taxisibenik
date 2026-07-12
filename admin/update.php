<?php
require __DIR__ . '/auth.php';
tx_require_login();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: index.php');
    exit;
}
tx_check_csrf();

$id     = (int) ($_POST['id'] ?? 0);
$action = $_POST['action'] ?? '';
$return = $_POST['return'] ?? 'index.php';
// Only allow returning to a local admin URL (list or a booking detail page).
if (!preg_match('/^(index|booking)\.php(\?[\w=&%.-]*)?$/', $return)) {
    $return = 'index.php';
}
// After a delete the detail page is gone; send back to the list.
if (($_POST['action'] ?? '') === 'delete') {
    $return = 'index.php';
}

$STATUSES = ['new', 'confirmed', 'completed', 'cancelled'];
$PAYMENTS = ['unpaid', 'deposit', 'paid'];

if ($id > 0) {
    if ($action === 'set_status' && in_array($_POST['value'] ?? '', $STATUSES, true)) {
        tx_db()->prepare('UPDATE bookings SET status = ? WHERE id = ?')->execute([$_POST['value'], $id]);
    } elseif ($action === 'set_payment' && in_array($_POST['value'] ?? '', $PAYMENTS, true)) {
        tx_db()->prepare('UPDATE bookings SET payment = ? WHERE id = ?')->execute([$_POST['value'], $id]);
    } elseif ($action === 'set_notes') {
        $notes = mb_substr(trim((string) ($_POST['value'] ?? '')), 0, 2000);
        tx_db()->prepare('UPDATE bookings SET admin_notes = ? WHERE id = ?')->execute([$notes === '' ? null : $notes, $id]);
    } elseif ($action === 'delete') {
        tx_db()->prepare('DELETE FROM bookings WHERE id = ?')->execute([$id]);
    }
}

header('Location: ' . $return);
exit;
