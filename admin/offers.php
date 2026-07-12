<?php
require __DIR__ . '/auth.php';
tx_require_login();

$offers = tx_db()->query(
    'SELECT * FROM offers ORDER BY (offer_date IS NULL), offer_date ASC, created_at DESC'
)->fetchAll();

$edit = null;
$editId = (int) ($_GET['edit'] ?? 0);
if ($editId > 0) {
    $s = tx_db()->prepare('SELECT * FROM offers WHERE id = ?');
    $s->execute([$editId]);
    $edit = $s->fetch() ?: null;
}
$csrf = tx_csrf_token();
function ev($v) { return $v === null ? '' : e($v); }
?>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Offers | TAXI Antonio Admin</title>
<link rel="stylesheet" href="admin.css">
</head>
<body class="admin-page">
  <header class="admin-header">
    <strong>TAXI Antonio &mdash; Offers</strong>
    <nav class="admin-nav">
      <a href="index.php">Bookings</a>
      <a href="offers.php" class="active">Offers</a>
      <a class="admin-logout" href="logout.php">Log out</a>
    </nav>
  </header>

  <div class="admin-wrap">
    <form class="offer-form" method="POST" action="offers-save.php">
      <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
      <input type="hidden" name="action" value="save">
      <input type="hidden" name="id" value="<?= $edit ? (int) $edit['id'] : 0 ?>">
      <h2><?= $edit ? 'Edit offer #' . (int) $edit['id'] : 'Add a new offer' ?></h2>

      <div class="offer-form-grid">
        <label>From (pickup)
          <input type="text" name="route_from" required value="<?= $edit ? ev($edit['route_from']) : '' ?>" placeholder="Skradin">
        </label>
        <label>To (destination)
          <input type="text" name="route_to" required value="<?= $edit ? ev($edit['route_to']) : '' ?>" placeholder="Split Airport">
        </label>
        <label>Date
          <input type="date" name="offer_date" value="<?= $edit ? ev($edit['offer_date']) : '' ?>">
        </label>
        <label>Pickup window start
          <input type="time" name="window_start" value="<?= $edit ? ev(substr((string) $edit['window_start'], 0, 5)) : '' ?>">
        </label>
        <label>Pickup window end
          <input type="time" name="window_end" value="<?= $edit ? ev(substr((string) $edit['window_end'], 0, 5)) : '' ?>">
        </label>
        <label>Offer price (&euro;)
          <input type="number" name="price" step="1" min="1" required value="<?= $edit ? (int) $edit['price'] : '' ?>">
        </label>
        <label>Normal price (&euro;, optional)
          <input type="number" name="original_price" step="1" min="1" value="<?= $edit && $edit['original_price'] !== null ? (int) $edit['original_price'] : '' ?>">
        </label>
        <label>Seats (optional)
          <input type="number" name="seats" step="1" min="1" max="12" value="<?= $edit && $edit['seats'] !== null ? (int) $edit['seats'] : '' ?>">
        </label>
        <label>Status
          <select name="status">
            <option value="active" <?= $edit && $edit['status'] === 'hidden' ? '' : 'selected' ?>>Active (shown)</option>
            <option value="hidden" <?= $edit && $edit['status'] === 'hidden' ? 'selected' : '' ?>>Hidden</option>
          </select>
        </label>
        <label class="offer-form-wide">Note (optional)
          <input type="text" name="note" maxlength="255" value="<?= $edit ? ev($edit['note']) : '' ?>" placeholder="e.g. empty return from an airport drop-off">
        </label>
      </div>

      <div class="offer-form-actions">
        <button type="submit" class="admin-btn"><?= $edit ? 'Save changes' : 'Add offer' ?></button>
        <?php if ($edit): ?><a class="admin-btn admin-btn-ghost" href="offers.php">Cancel</a><?php endif; ?>
      </div>
    </form>

    <h2 class="offer-list-title">Current offers (<?= count($offers) ?>)</h2>
    <?php if (!$offers): ?>
      <p class="admin-empty">No offers yet. Add one above and it appears on /special-offers/.</p>
    <?php endif; ?>

    <?php foreach ($offers as $o): ?>
      <article class="offer-admin-card <?= $o['status'] === 'hidden' ? 'is-hidden' : '' ?>">
        <div class="offer-admin-main">
          <span class="offer-admin-route"><?= e($o['route_from']) ?> &rarr; <?= e($o['route_to']) ?></span>
          <span class="offer-admin-when">
            <?= $o['offer_date'] ? e(date('D j M Y', strtotime($o['offer_date']))) : 'Flexible date' ?>
            <?php if ($o['window_start'] && $o['window_end']): ?>
              &middot; <?= e(substr($o['window_start'], 0, 5)) ?>&ndash;<?= e(substr($o['window_end'], 0, 5)) ?>
            <?php endif; ?>
          </span>
          <span class="offer-admin-price">
            <?php if ($o['original_price'] !== null): ?><s>&euro;<?= (int) $o['original_price'] ?></s> <?php endif; ?>
            <strong>&euro;<?= (int) $o['price'] ?></strong>
            <?php if ($o['seats'] !== null): ?><em>up to <?= (int) $o['seats'] ?></em><?php endif; ?>
          </span>
          <?php if ($o['note']): ?><span class="offer-admin-note"><?= e($o['note']) ?></span><?php endif; ?>
          <?php if ($o['status'] === 'hidden'): ?><span class="offer-admin-badge">Hidden</span><?php endif; ?>
        </div>
        <div class="offer-admin-actions">
          <a class="admin-btn admin-btn-ghost" href="offers.php?edit=<?= (int) $o['id'] ?>">Edit</a>
          <form method="POST" action="offers-save.php" class="inline-form">
            <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
            <input type="hidden" name="id" value="<?= (int) $o['id'] ?>">
            <input type="hidden" name="action" value="toggle">
            <button type="submit" class="admin-btn admin-btn-ghost"><?= $o['status'] === 'hidden' ? 'Show' : 'Hide' ?></button>
          </form>
          <form method="POST" action="offers-save.php" class="inline-form" onsubmit="return confirm('Delete this offer?');">
            <input type="hidden" name="csrf" value="<?= e($csrf) ?>">
            <input type="hidden" name="id" value="<?= (int) $o['id'] ?>">
            <input type="hidden" name="action" value="delete">
            <button type="submit" class="admin-link-danger">Delete</button>
          </form>
        </div>
      </article>
    <?php endforeach; ?>
  </div>
</body>
</html>
