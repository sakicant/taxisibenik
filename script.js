const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

const whatsappFloat = document.getElementById('whatsapp-float');
if (whatsappFloat) {
  setTimeout(() => whatsappFloat.classList.add('visible'), 3000);
}

const siteHeader = document.querySelector('.site-header');
if (siteHeader) {
  const toggleHeaderBg = () => siteHeader.classList.toggle('scrolled', window.scrollY > 40);
  toggleHeaderBg();
  window.addEventListener('scroll', toggleHeaderBg);
}

const navToggle = document.getElementById('nav-toggle');
const mainNav = document.getElementById('main-nav');
if (navToggle && mainNav) {
  navToggle.addEventListener('click', () => {
    const isOpen = mainNav.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });
}

document.querySelectorAll('.nav-dropdown-toggle').forEach((toggle) => {
  toggle.addEventListener('click', () => {
    if (window.innerWidth > 900) return;
    const dropdown = toggle.closest('.nav-dropdown');
    dropdown.classList.toggle('open');
  });
});

const quoteWidget = document.getElementById('quote-widget');
if (quoteWidget) {
  const ROUTES = [
    ['Šibenik', 'Split Airport', 95],
    ['Šibenik', 'Split', 140],
    ['Šibenik', 'Zadar Airport', 130],
    ['Šibenik', 'Zadar', 140],
    ['Šibenik', 'Zagreb', 500],
    ['Šibenik', 'Dubrovnik', 500],
    ['Šibenik', 'Trogir', 95],
    ['Šibenik', 'Vodice', 30],
    ['Šibenik', 'Skradin', 50],
    ['Šibenik', 'Primošten', 50],
    ['Šibenik', 'Makarska', 210],
    ['Split Airport', 'Vodice', 115],
    ['Split Airport', 'Zadar', 210],
    ['Split Airport', 'Novalja', 250],
    ['Split', 'Vodice', 155],
    ['Split', 'Zadar', 230],
    ['Split', 'Zadar Airport', 210],
    ['Zadar Airport', 'Vodice', 100],
    ['Zadar Airport', 'Primošten', 160],
    ['Zadar Airport', 'Dubrovnik', 550],
    ['Zadar', 'Dubrovnik', 550]
  ];

  const LOCATIONS = ['Šibenik'];
  ROUTES.forEach(([a, b]) => {
    if (!LOCATIONS.includes(a)) LOCATIONS.push(a);
    if (!LOCATIONS.includes(b)) LOCATIONS.push(b);
  });

  const fromSelect = document.getElementById('quote-from');
  const toSelect = document.getElementById('quote-to');
  [fromSelect, toSelect].forEach((select) => {
    LOCATIONS.forEach((loc) => {
      const opt = document.createElement('option');
      opt.value = loc;
      opt.textContent = loc;
      select.appendChild(opt);
    });
  });

  function findRoute(from, to) {
    return ROUTES.find(([a, b]) => (a === from && b === to) || (a === to && b === from));
  }

  const tripToggleBtns = document.querySelectorAll('.trip-toggle-btn');
  let tripType = 'oneway';
  tripToggleBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      tripToggleBtns.forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');
      tripType = btn.dataset.trip;
    });
  });

  document.querySelectorAll('.stepper-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      const target = document.getElementById(btn.dataset.target);
      const delta = parseInt(btn.dataset.delta, 10);
      const min = parseInt(target.dataset.min, 10);
      const max = parseInt(target.dataset.max, 10);
      const next = Math.min(max, Math.max(min, parseInt(target.dataset.value, 10) + delta));
      target.dataset.value = String(next);
      target.textContent = String(next);
    });
  });

  // Price for one specific direction. The table is currently symmetric, so both
  // directions return the same number; kept directional so asymmetric arriving/
  // departing prices can be added later without changing the return-sum logic.
  function priceFor(a, b) {
    const r = findRoute(a, b);
    return r ? r[2] : null;
  }

  function bookingUrl(q) {
    const params = new URLSearchParams();
    params.set('from', q.from);
    params.set('to', q.to);
    params.set('trip', q.tripType);
    params.set('pax', q.passengers);
    params.set('lug', q.luggage);
    params.set('price', q.priceParam);
    return '/book/?' + params.toString();
  }

  const quoteResult = document.getElementById('quote-result');

  document.getElementById('quote-submit').addEventListener('click', () => {
    const from = fromSelect.value;
    const to = toSelect.value;

    quoteResult.hidden = false;

    if (!from || !to) {
      quoteResult.innerHTML = '<p>Please choose a pickup location and destination.</p>';
      return;
    }

    const passengers = document.getElementById('quote-passengers').dataset.value;
    const luggage = document.getElementById('quote-luggage').dataset.value;
    const base = { from, to, tripType, passengers, luggage };

    if (from === to) {
      const url = bookingUrl({ ...base, priceParam: 'meter' });
      quoteResult.innerHTML =
        '<p>A local ride within ' + from + ' is charged by the taxi meter, from &euro;10. See the <a href="#pricing">local rates</a> below.</p>' +
        '<a class="btn btn-primary quote-btn" href="' + url + '">Book Now</a>';
      return;
    }

    const oneway = priceFor(from, to);
    if (oneway != null) {
      let total, sub;
      if (tripType === 'return') {
        total = oneway + priceFor(to, from);
        sub = 'return total';
      } else {
        total = oneway;
        sub = 'one way';
      }
      const url = bookingUrl({ ...base, priceParam: String(total) });
      quoteResult.innerHTML =
        '<div class="quote-price">&euro;' + total + ' <span class="quote-price-sub">' + sub + '</span></div>' +
        '<a class="btn btn-primary quote-btn" href="' + url + '">Book Now</a>';
    } else {
      const url = bookingUrl({ ...base, priceParam: 'custom' });
      quoteResult.innerHTML =
        '<p>I don\'t have a listed fixed price for ' + from + ' to ' + to + ' yet, but I\'ll quote you directly.</p>' +
        '<a class="btn btn-primary quote-btn" href="' + url + '">Request a Quote</a>';
    }
  });
}

// Booking page: reads the quote from the URL, shows a summary, collects the
// remaining details (date, time, contact) and emails the full request.
const bookingPageForm = document.getElementById('booking-page-form');
if (bookingPageForm) {
  const params = new URLSearchParams(location.search);
  const from = params.get('from') || '';
  const to = params.get('to') || '';
  const trip = params.get('trip') || 'oneway';
  const pax = params.get('pax') || '1';
  const lug = params.get('lug') || '0';
  const priceParam = params.get('price') || '';
  const isReturn = trip === 'return';

  document.getElementById('book-return-fields').hidden = !isReturn;

  let priceText;
  if (priceParam === 'meter') priceText = 'Taxi meter (from €10)';
  else if (priceParam === 'custom' || priceParam === '') priceText = 'Custom quote';
  else priceText = '€' + priceParam;

  if (from && to) {
    document.getElementById('booking-summary').hidden = false;
    document.getElementById('sum-from').textContent = from;
    document.getElementById('sum-to').textContent = to;
    document.getElementById('sum-trip').textContent = isReturn ? 'Return' : 'One way';
    document.getElementById('sum-passengers').textContent = pax;
    document.getElementById('sum-luggage').textContent = lug;
    document.getElementById('sum-price').textContent = priceText;
    if (priceParam === 'meter' || priceParam === 'custom' || priceParam === '') {
      document.getElementById('sum-note').textContent = 'This route is priced individually. I\'ll confirm your exact fare by email.';
    }
  }

  const bookingPageNote = document.getElementById('booking-page-note');
  bookingPageForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('book-name').value.trim();
    const email = document.getElementById('book-email').value.trim();
    const date = document.getElementById('book-date').value;
    const time = document.getElementById('book-time').value;

    if (!name || !email || !date || !time) {
      bookingPageNote.textContent = 'Please fill in your name, email, pickup date, and time.';
      return;
    }

    const phone = document.getElementById('book-phone').value.trim();
    const flight = document.getElementById('book-flight').value.trim();
    const notes = document.getElementById('book-notes').value.trim();
    const rDate = document.getElementById('book-return-date').value;
    const rTime = document.getElementById('book-return-time').value;

    const lines = [
      'New booking request from taxisibenik.hr:',
      '',
      'From: ' + (from || 'Not specified'),
      'To: ' + (to || 'Not specified'),
      'Trip type: ' + (isReturn ? 'Return' : 'One way'),
      'Passengers: ' + pax,
      'Luggage: ' + lug,
      'Quoted price: ' + priceText,
      'Pickup date: ' + date,
      'Pickup time: ' + time
    ];
    if (isReturn) {
      lines.push('Return date: ' + (rDate || 'not specified'));
      lines.push('Return time: ' + (rTime || 'not specified'));
    }
    if (flight) lines.push('Flight/vessel: ' + flight);
    if (notes) lines.push('', 'Notes: ' + notes);

    bookingPageNote.textContent = 'Sending...';

    try {
      const body = new FormData();
      body.append('name', name);
      body.append('email', email);
      body.append('phone', phone);
      body.append('message', lines.join('\n'));

      const response = await fetch('/contact.php', {
        method: 'POST',
        body,
        headers: { Accept: 'application/json' }
      });
      const data = await response.json().catch(() => null);

      if (response.ok && data && data.success) {
        bookingPageNote.textContent = 'Thanks! Your booking request has been sent. Antonio will confirm shortly.';
        bookingPageForm.reset();
      } else {
        bookingPageNote.textContent = (data && data.error) || 'Something went wrong. Please call or WhatsApp me instead.';
      }
    } catch (err) {
      bookingPageNote.textContent = 'Something went wrong. Please call or WhatsApp me instead.';
    }
  });
}

const form = document.getElementById('contact-form');
const note = document.getElementById('form-note');

if (form && note) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    note.textContent = 'Sending...';

    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      });

      const data = await response.json().catch(() => null);

      if (response.ok && data && data.success) {
        note.textContent = 'Thanks! Your message has been sent. Antonio will get back to you shortly.';
        form.reset();
      } else {
        note.textContent = (data && data.error) || 'Something went wrong. Please call or WhatsApp me instead.';
      }
    } catch (err) {
      note.textContent = 'Something went wrong. Please call or WhatsApp me instead.';
    }
  });
}
