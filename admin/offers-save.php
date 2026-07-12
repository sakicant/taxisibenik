<?php
/**
 * Create / update / delete / toggle special offers. Admin only.
 */
require __DIR__ . '/auth.php';
tx_require_login();

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Location: offers.php');
    exit;
}
tx_check_csrf();

$action = $_POST['action'] ?? '';
$id     = (int) ($_POST['id'] ?? 0);

if ($action === 'delete' && $id > 0) {
    tx_db()->prepare('DELETE FROM offers WHERE id = ?')->execute([$id]);
} elseif ($action === 'toggle' && $id > 0) {
    tx_db()->prepare("UPDATE offers SET status = IF(status = 'active', 'hidden', 'active') WHERE id = ?")->execute([$id]);
} elseif ($action === 'save') {
    $from   = mb_substr(trim((string) ($_POST['route_from'] ?? '')), 0, 120);
    $to     = mb_substr(trim((string) ($_POST['route_to'] ?? '')), 0, 120);
    $date   = trim((string) ($_POST['offer_date'] ?? '')) ?: null;
    $ws     = trim((string) ($_POST['window_start'] ?? '')) ?: null;
    $we     = trim((string) ($_POST['window_end'] ?? '')) ?: null;
    $price  = (float) ($_POST['price'] ?? 0);
    $origIn = trim((string) ($_POST['original_price'] ?? ''));
    $orig   = $origIn === '' ? null : (float) $origIn;
    $seatIn = trim((string) ($_POST['seats'] ?? ''));
    $seats  = $seatIn === '' ? null : max(1, min(12, (int) $seatIn));
    $note   = mb_substr(trim((string) ($_POST['note'] ?? '')), 0, 255) ?: null;
    $status = ($_POST['status'] ?? 'active') === 'hidden' ? 'hidden' : 'active';

    if ($from !== '' && $to !== '' && $price > 0) {
        if ($id > 0) {
            tx_db()->prepare(
                'UPDATE offers SET route_from=?, route_to=?, offer_date=?, window_start=?, window_end=?,
                 price=?, original_price=?, seats=?, note=?, status=? WHERE id=?'
            )->execute([$from, $to, $date, $ws, $we, $price, $orig, $seats, $note, $status, $id]);
        } else {
            tx_db()->prepare(
                'INSERT INTO offers (route_from, route_to, offer_date, window_start, window_end,
                 price, original_price, seats, note, status) VALUES (?,?,?,?,?,?,?,?,?,?)'
            )->execute([$from, $to, $date, $ws, $we, $price, $orig, $seats, $note, $status]);
        }
    }
}

header('Location: offers.php');
exit;
