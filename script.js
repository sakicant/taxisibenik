const yearEl = document.getElementById('year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

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
