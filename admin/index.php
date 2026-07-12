<?php
require __DIR__ . '/auth.php';
tx_require_login();

$STATUSES = ['new', 'confirmed', 'completed', 'cancelled'];
$PAYMENTS = ['unpaid' => 'Unpaid', 'deposit' => 'Deposit paid', 'paid' => 'Paid in full'];

$statusFilter = $_GET['status'] ?? '';
$q = trim($_GET['q'] ?? '');

$where = [];
$params = [];
if (in_array($statusFilter, $STATUSES, true)) {
    $where[] = 'status = ?';
    $params[] = $statusFilter;
}
if ($q !== '') {
    $where[] = '(customer_name LIKE ? OR customer_email LIKE ? OR pickup LIKE ? OR dropoff LIKE ?)';
    $like = '%' . $q . '%';
    array_push($params, $like, $like, $like, $like);
}
$sql = 'SELECT * FROM bookings';
if ($where) $sql .= ' WHERE ' . implode(' AND ', $where);
$sql .= ' ORDER BY created_at DESC LIMIT 500';
$stmt = tx_db()->prepare($sql);
$stmt->execute($params);
$bookings = $stmt->fetchAll();

// Counts per status for the filter chips.
$counts = ['all' => 0, 'new' => 0, 'confirmed' => 0, 'completed' => 0, 'cancelled' => 0];
foreach (tx_db()->query('SELECT status, COUNT(*) c FROM bookings GROUP BY status') as $r) {
    $counts[$r['status']] = (int) $r['c'];
    $counts['all'] += (int) $r['c'];
}

$csrf = tx_csrf_token();
$returnUrl = 'index.php' . ($_SERVER['QUERY_STRING'] ? '?' . $_SERVER['QUERY_STRING'] : '');

function chip_url($status)
{
    $params = $_GET;
    if ($status === '') unset($params['status']); else $params['status'] = $status;
    return 'index.php' . ($params ? '?' . http_build_query($params) : '');
}
function fmt_dt($date, $time)
{
    if (!$date) return '&mdash;';
    return e($date) . ($time ? ' ' . e(substr($time, 0, 5)) : '');
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Bookings | TAXI Antonio Admin</title>
<link rel="stylesheet" href="admin.css">
</head>
<body class="admin-page">
  <header class="admin-header">
    <strong>TAXI Antonio &mdash; Bookings</strong>
    <nav class="admin-nav">
      <a href="index.php" class="active">Bookings</a>
      <a href="offers.php">Offers</a>
      <a class="admin-logout" href="logout.php">Log out</a>
    </nav>
  </header>

  <div class="admin-wrap">
    <form class="admin-search" method="GET" action="index.php">
      <?php if ($statusFilter): ?><input type="hidden" name="status" value="<?= e($statusFilter) ?>"><?php endif; ?>
      <input type="search" name="q" placeholder="Search name, email, route..." value="<?= e($q) ?>">
      <button type="submit" class="admin-btn">Search</button>
      <?php if ($q): ?><a class="admin-btn admin-btn-ghost" href="<?= e(chip_url($statusFilter)) ?>">Clear</a><?php endif; ?>
    </form>

    <nav class="admin-chips">
      <a class="admin-chip <?= $statusFilter === '' ? 'active' : '' ?>" href="<?= e(chip_url('')) ?>">All (<?= $counts['all'] ?>)</a>
      <?php foreach ($STATUSES as $s): ?>
        <a class="admin-chip <?= $statusFilter === $s ? 'active' : '' ?>" href="<?= e(chip_url($s)) ?>"><?= ucfirst($s) ?> (<?= $counts[$s] ?>)</a>
      <?php endforeach; ?>
    </nav>

    <?php if (!$bookings): ?>
      <p class="admin-empty">No bookings found.</p>
    <?php endif; ?>

    <?php foreach ($bookings as $b): ?>
      <article class="booking-card status-<?= e($b['status']) ?>">
        <div class="booking-head">
          <div>
            <span class="booking-id">#<?= (int) $b['id'] ?></span>
            <span class="booking-route"><?= e($b['pickup']) ?> &rarr; <?= e($b['dropoff']) ?></span>
            <span class="booking-trip"><?= $b['trip_type'] === 'return' ? 'Return' : 'One way' ?></span>
          </div>
          <span class="booking-received">received <?= e(date('j M Y H:i', strtotime($b['created_at']))) ?></span>
        </div>

        <div class="booking-grid">
          <div><span>Pickup</span><strong><?= fmt_dt($b['pickup_date'], $b['pickup_time']) ?></strong></div>
          <?php if ($b['trip_type'] === 'return'): ?>
          <div><span>Return</span><strong><?= fmt_dt($b['return_date'], $b['return_time']) ?></strong></div>
          <?php endif; ?>
          <div><span>Passengers</span><strong><?= (int) $b['passengers'] ?></strong></div>
          <div><span>Luggage</span><strong><?= (int) $b['luggage'] ?></strong></div>
          <div><span>Quoted price</span><strong><?= $b['quoted_price'] ? e($b['quoted_price']) : 'custom' ?></strong></div>
          <div><span>Name</span><strong><?= e($b['customer_name']) ?></strong></div>
          <div><span>Email</span><strong><a href="mailto:<?= e($b['customer_email']) ?>"><?= e($b['customer_email']) ?></a></strong></div>
          <div><span>Phone</span><strong><?= $b['customer_phone'] ? e($b['customer_phone']) : '&mdash;' ?></strong></div>
          <?php if ($b['flight']): ?><div><span>Pickup details</span><strong><?= e($b['flight']) ?></strong></div><?php endif; ?>
          <?php if (!empty($b['dropoff_details'])): ?><div><span>Destination details</span><strong><?= e($b['dropoff_details']) ?></strong></div><?php endif; ?>
        </div>

        <?php if ($b['notes']): ?><p class="booking-notes"><span>Customer notes:</span> <?= e($b['notes']) ?></p><?php endif; ?>

        <div class="booking-actions">
          <form method="POST" action="update.php" class="inline-form">
            <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
            <input type="hidden" name="id" value="<?= (int) $b['id'] ?>">
            <input type="hidden" name="return" value="<?= e($returnUrl) ?>">
            <input type="hidden" name="action" value="set_status">
            <label>Status
              <select name="value" onchange="this.form.submit()">
                <?php foreach ($STATUSES as $s): ?>
                  <option value="<?= $s ?>" <?= $b['status'] === $s ? 'selected' : '' ?>><?= ucfirst($s) ?></option>
                <?php endforeach; ?>
              </select>
            </label>
          </form>

          <form method="POST" action="update.php" class="inline-form">
            <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
            <input type="hidden" name="id" value="<?= (int) $b['id'] ?>">
            <input type="hidden" name="return" value="<?= e($returnUrl) ?>">
            <input type="hidden" name="action" value="set_payment">
            <label>Payment
              <select name="value" onchange="this.form.submit()">
                <?php foreach ($PAYMENTS as $val => $lbl): ?>
                  <option value="<?= $val ?>" <?= $b['payment'] === $val ? 'selected' : '' ?>><?= $lbl ?></option>
                <?php endforeach; ?>
              </select>
            </label>
          </form>
        </div>

        <form method="POST" action="update.php" class="booking-adminnotes">
          <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
          <input type="hidden" name="id" value="<?= (int) $b['id'] ?>">
          <input type="hidden" name="return" value="<?= e($returnUrl) ?>">
          <input type="hidden" name="action" value="set_notes">
          <textarea name="value" rows="2" placeholder="Private notes (only you see these)..."><?= e($b['admin_notes']) ?></textarea>
          <button type="submit" class="admin-btn admin-btn-ghost">Save note</button>
        </form>

        <form method="POST" action="update.php" class="booking-delete" onsubmit="return confirm('Delete booking #<?= (int) $b['id'] ?>? This cannot be undone.');">
          <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
          <input type="hidden" name="id" value="<?= (int) $b['id'] ?>">
          <input type="hidden" name="return" value="<?= e($returnUrl) ?>">
          <input type="hidden" name="action" value="delete">
          <button type="submit" class="admin-link-danger">Delete</button>
        </form>
      </article>
    <?php endforeach; ?>
  </div>
</body>
</html>
