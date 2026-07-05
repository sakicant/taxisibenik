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
  const PRICES = {
    "Split Airport (SPU)": {
      "Zadar Airport (ZAD)": 200,
      "Šibenik - center": 95,
      "Amadria Park Hotel Šibenik": 95,
      "D-Resort Hotel Šibenik": 95,
      "D-Marin Marina Mandalina Šibenik": 95,
      "Vodice": 115,
      "Tisno": 130,
      "Zadar": 210,
      "Primošten": 80,
      "Srima": 115,
      "NP Krka - Skradin entrance": 110,
      "NP Krka - Lozovac entrance": 95,
      "NP Krka - Roški Slap entrance": 100,
      "Žaborić": 95,
      "Grebaštica": 90,
      "Zaton": 115,
      "Dubrovnik": 450,
      "Zagreb": 550,
      "Brodarica - Šibenik": 95,
      "Bilice": 100,
      "Dubrovnik Airport (DBV)": 450,
      "Zagreb Airport (ZAG)": 550,
      "NP Plitvice Lakes": 395,
      "Skradin - center": 110,
      "Marina ACI Skradin": 100,
      "Marina Zaton": 115,
      "Betina": 150,
      "Pirovac": 125,
      "Murter": 150,
      "Bilo": 80,
      "Jadrija": 115,
      "Jezera": 135,
      "Rogoznica": 80,
      "Tribunj": 120
    },
    "Zadar Airport (ZAD)": {
      "Split Airport (SPU)": 200,
      "Šibenik - center": 130,
      "Amadria Park Hotel Šibenik": 130,
      "D-Resort Hotel Šibenik": 130,
      "D-Marin Marina Mandalina Šibenik": 130,
      "Split": 210,
      "Primošten": 160,
      "NP Krka - Skradin entrance": 105,
      "NP Krka - Lozovac entrance": 120,
      "NP Krka - Roški Slap entrance": 110,
      "Skradin - center": 105,
      "Marina ACI Skradin": 99
    },
    "Šibenik - center": {
      "Split Airport (SPU)": 95,
      "Zadar Airport (ZAD)": 130,
      "Amadria Park Hotel Šibenik": 18,
      "D-Resort Hotel Šibenik": 15,
      "D-Marin Marina Mandalina Šibenik": 15,
      "Vodice": 30,
      "Tisno": 50,
      "Zadar": 140,
      "Split": 140,
      "Primošten": 50,
      "Srima": 25,
      "NP Krka - Skradin entrance": 50,
      "NP Krka - Lozovac entrance": 45,
      "NP Krka - Roški Slap entrance": 90,
      "Žaborić": 25,
      "Grebaštica": 35,
      "Zaton": 25,
      "Dubrovnik": 480,
      "Zagreb": 480,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 310,
      "Skradin - center": 50,
      "Marina ACI Skradin": 50,
      "Marina Zaton": 20,
      "Betina": 70,
      "Pirovac": 50,
      "Murter": 70,
      "Bilo": 40,
      "Jadrija": 30,
      "Jezera": 55,
      "Rogoznica": 65,
      "Trogir": 95,
      "Tribunj": 40
    },
    "Amadria Park Hotel Šibenik": {
      "Split Airport (SPU)": 95,
      "Zadar Airport (ZAD)": 130,
      "Šibenik - center": 18,
      "D-Resort Hotel Šibenik": 18,
      "D-Marin Marina Mandalina Šibenik": 18,
      "Vodice": 40,
      "Tisno": 55,
      "Zadar": 140,
      "Split": 140,
      "Primošten": 50,
      "Srima": 35,
      "NP Krka - Skradin entrance": 50,
      "NP Krka - Lozovac entrance": 45,
      "NP Krka - Roški Slap entrance": 90,
      "Žaborić": 28,
      "Grebaštica": 35,
      "Zaton": 35,
      "Dubrovnik": 480,
      "Zagreb": 480,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 310,
      "Skradin - center": 50,
      "Marina ACI Skradin": 50,
      "Marina Zaton": 30,
      "Betina": 80,
      "Pirovac": 55,
      "Murter": 80,
      "Bilo": 40,
      "Jadrija": 40,
      "Jezera": 65,
      "Rogoznica": 65,
      "Trogir": 95,
      "Tribunj": 45
    },
    "D-Resort Hotel Šibenik": {
      "Split Airport (SPU)": 95,
      "Zadar Airport (ZAD)": 130,
      "Šibenik - center": 15,
      "Amadria Park Hotel Šibenik": 18,
      "Vodice": 35,
      "Tisno": 55,
      "Zadar": 140,
      "Split": 140,
      "Primošten": 50,
      "Srima": 30,
      "NP Krka - Skradin entrance": 50,
      "NP Krka - Lozovac entrance": 45,
      "NP Krka - Roški Slap entrance": 90,
      "Žaborić": 25,
      "Grebaštica": 35,
      "Zaton": 35,
      "Dubrovnik": 480,
      "Zagreb": 480,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 310,
      "Skradin - center": 50,
      "Marina ACI Skradin": 50,
      "Marina Zaton": 30,
      "Betina": 70,
      "Pirovac": 50,
      "Murter": 70,
      "Bilo": 40,
      "Jadrija": 40,
      "Jezera": 60,
      "Rogoznica": 65,
      "Trogir": 95,
      "Tribunj": 40
    },
    "D-Marin Marina Mandalina Šibenik": {
      "Split Airport (SPU)": 95,
      "Zadar Airport (ZAD)": 130,
      "Šibenik - center": 15,
      "Amadria Park Hotel Šibenik": 18,
      "Vodice": 35,
      "Tisno": 55,
      "Zadar": 140,
      "Split": 140,
      "Primošten": 50,
      "Srima": 30,
      "NP Krka - Skradin entrance": 50,
      "NP Krka - Lozovac entrance": 45,
      "NP Krka - Roški Slap entrance": 90,
      "Žaborić": 25,
      "Grebaštica": 35,
      "Zaton": 35,
      "Dubrovnik": 480,
      "Zagreb": 480,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 310,
      "Skradin - center": 50,
      "Marina ACI Skradin": 50,
      "Marina Zaton": 30,
      "Betina": 70,
      "Pirovac": 50,
      "Murter": 70,
      "Bilo": 40,
      "Jadrija": 40,
      "Jezera": 60,
      "Rogoznica": 65,
      "Trogir": 95,
      "Tribunj": 40
    },
    "Vodice": {
      "Split Airport (SPU)": 115,
      "Šibenik - center": 30,
      "Amadria Park Hotel Šibenik": 40,
      "D-Resort Hotel Šibenik": 35,
      "D-Marin Marina Mandalina Šibenik": 35,
      "NP Krka - Skradin entrance": 60,
      "NP Krka - Lozovac entrance": 60,
      "NP Krka - Roški Slap entrance": 90,
      "Skradin - center": 60,
      "Marina ACI Skradin": 70
    },
    "Tisno": {
      "Split Airport (SPU)": 130,
      "Šibenik - center": 50,
      "Amadria Park Hotel Šibenik": 55,
      "D-Resort Hotel Šibenik": 55,
      "D-Marin Marina Mandalina Šibenik": 55,
      "NP Krka - Skradin entrance": 65,
      "NP Krka - Lozovac entrance": 80,
      "NP Krka - Roški Slap entrance": 90,
      "Skradin - center": 65,
      "Marina ACI Skradin": 90
    },
    "Zadar": {
      "Split Airport (SPU)": 210,
      "Šibenik - center": 140,
      "Amadria Park Hotel Šibenik": 140,
      "D-Resort Hotel Šibenik": 140,
      "D-Marin Marina Mandalina Šibenik": 140,
      "Split": 230,
      "NP Krka - Skradin entrance": 130,
      "NP Krka - Lozovac entrance": 145,
      "NP Krka - Roški Slap entrance": 135,
      "Skradin - center": 130,
      "Marina ACI Skradin": 130
    },
    "Split": {
      "Zadar Airport (ZAD)": 210,
      "Šibenik - center": 140,
      "Amadria Park Hotel Šibenik": 140,
      "D-Resort Hotel Šibenik": 140,
      "D-Marin Marina Mandalina Šibenik": 140,
      "Zadar": 230,
      "NP Krka - Skradin entrance": 140,
      "NP Krka - Lozovac entrance": 145,
      "NP Krka - Roški Slap entrance": 150,
      "Skradin - center": 140,
      "Marina ACI Skradin": 140
    },
    "Primošten": {
      "Split Airport (SPU)": 80,
      "Zadar Airport (ZAD)": 160,
      "Šibenik - center": 50,
      "Amadria Park Hotel Šibenik": 50,
      "D-Resort Hotel Šibenik": 50,
      "D-Marin Marina Mandalina Šibenik": 50,
      "NP Krka - Skradin entrance": 80,
      "NP Krka - Lozovac entrance": 80,
      "NP Krka - Roški Slap entrance": 110,
      "Skradin - center": 80,
      "Marina ACI Skradin": 85
    },
    "Srima": {
      "Split Airport (SPU)": 115,
      "Šibenik - center": 25,
      "Amadria Park Hotel Šibenik": 35,
      "D-Resort Hotel Šibenik": 30,
      "D-Marin Marina Mandalina Šibenik": 30,
      "NP Krka - Skradin entrance": 65,
      "NP Krka - Lozovac entrance": 55,
      "NP Krka - Roški Slap entrance": 90,
      "Skradin - center": 65,
      "Marina ACI Skradin": 65
    },
    "NP Krka - Skradin entrance": {
      "Split Airport (SPU)": 110,
      "Zadar Airport (ZAD)": 105,
      "Šibenik - center": 50,
      "Amadria Park Hotel Šibenik": 50,
      "D-Resort Hotel Šibenik": 50,
      "D-Marin Marina Mandalina Šibenik": 50,
      "Vodice": 60,
      "Tisno": 65,
      "Zadar": 130,
      "Split": 140,
      "Primošten": 80,
      "Srima": 65,
      "NP Krka - Lozovac entrance": 25,
      "NP Krka - Roški Slap entrance": 50,
      "Žaborić": 75,
      "Grebaštica": 80,
      "Zaton": 60,
      "Dubrovnik": 480,
      "Zagreb": 480,
      "Brodarica - Šibenik": 55,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 290,
      "Marina Zaton": 55,
      "Betina": 75,
      "Pirovac": 65,
      "Murter": 75,
      "Bilo": 85,
      "Jadrija": 75,
      "Jezera": 70,
      "Rogoznica": 90,
      "Trogir": 100,
      "Tribunj": 60
    },
    "NP Krka - Lozovac entrance": {
      "Split Airport (SPU)": 95,
      "Zadar Airport (ZAD)": 120,
      "Šibenik - center": 45,
      "Amadria Park Hotel Šibenik": 45,
      "D-Resort Hotel Šibenik": 45,
      "D-Marin Marina Mandalina Šibenik": 45,
      "Vodice": 60,
      "Tisno": 80,
      "Zadar": 145,
      "Split": 145,
      "Primošten": 80,
      "Srima": 55,
      "NP Krka - Skradin entrance": 25,
      "NP Krka - Roški Slap entrance": 65,
      "Žaborić": 55,
      "Grebaštica": 75,
      "Zaton": 60,
      "Dubrovnik": 500,
      "Zagreb": 500,
      "Brodarica - Šibenik": 55,
      "Bilice": 40,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 310,
      "Skradin - center": 25,
      "Marina ACI Skradin": 25,
      "Marina Zaton": 65,
      "Betina": 85,
      "Pirovac": 80,
      "Murter": 100,
      "Bilo": 80,
      "Jadrija": 70,
      "Jezera": 90,
      "Rogoznica": 95,
      "Trogir": 95,
      "Tribunj": 70
    },
    "NP Krka - Roški Slap entrance": {
      "Split Airport (SPU)": 100,
      "Zadar Airport (ZAD)": 110,
      "Šibenik - center": 90,
      "Amadria Park Hotel Šibenik": 90,
      "D-Resort Hotel Šibenik": 90,
      "D-Marin Marina Mandalina Šibenik": 90,
      "Vodice": 90,
      "Tisno": 90,
      "Zadar": 135,
      "Split": 150,
      "Primošten": 110,
      "Srima": 90,
      "NP Krka - Skradin entrance": 50,
      "NP Krka - Lozovac entrance": 65,
      "Žaborić": 115,
      "Grebaštica": 90,
      "Zaton": 75,
      "Dubrovnik": 500,
      "Zagreb": 500,
      "Brodarica - Šibenik": 80,
      "Bilice": 80,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 290,
      "Skradin - center": 50,
      "Marina ACI Skradin": 50,
      "Marina Zaton": 75,
      "Betina": 115,
      "Pirovac": 85,
      "Murter": 115,
      "Bilo": 125,
      "Jadrija": 100,
      "Jezera": 95,
      "Rogoznica": 120,
      "Trogir": 110,
      "Tribunj": 95
    },
    "Žaborić": {
      "Split Airport (SPU)": 95,
      "Šibenik - center": 25,
      "Amadria Park Hotel Šibenik": 28,
      "D-Resort Hotel Šibenik": 25,
      "D-Marin Marina Mandalina Šibenik": 25,
      "NP Krka - Skradin entrance": 75,
      "NP Krka - Lozovac entrance": 55,
      "NP Krka - Roški Slap entrance": 115,
      "Skradin - center": 75,
      "Marina ACI Skradin": 75
    },
    "Grebaštica": {
      "Split Airport (SPU)": 90,
      "Šibenik - center": 35,
      "Amadria Park Hotel Šibenik": 35,
      "D-Resort Hotel Šibenik": 35,
      "D-Marin Marina Mandalina Šibenik": 35,
      "NP Krka - Skradin entrance": 80,
      "NP Krka - Lozovac entrance": 75,
      "NP Krka - Roški Slap entrance": 90,
      "Skradin - center": 80,
      "Marina ACI Skradin": 80
    },
    "Zaton": {
      "Split Airport (SPU)": 115,
      "Šibenik - center": 25,
      "Amadria Park Hotel Šibenik": 35,
      "D-Resort Hotel Šibenik": 35,
      "D-Marin Marina Mandalina Šibenik": 35,
      "NP Krka - Skradin entrance": 60,
      "NP Krka - Lozovac entrance": 60,
      "NP Krka - Roški Slap entrance": 75,
      "Skradin - center": 60,
      "Marina ACI Skradin": 60
    },
    "Dubrovnik": {
      "Split Airport (SPU)": 450,
      "Šibenik - center": 480,
      "Amadria Park Hotel Šibenik": 480,
      "D-Resort Hotel Šibenik": 480,
      "D-Marin Marina Mandalina Šibenik": 480,
      "NP Krka - Skradin entrance": 480,
      "NP Krka - Lozovac entrance": 500,
      "NP Krka - Roški Slap entrance": 500,
      "Skradin - center": 480,
      "Marina ACI Skradin": 500
    },
    "Zagreb": {
      "Split Airport (SPU)": 550,
      "Šibenik - center": 480,
      "Amadria Park Hotel Šibenik": 480,
      "D-Resort Hotel Šibenik": 480,
      "D-Marin Marina Mandalina Šibenik": 480,
      "NP Krka - Skradin entrance": 480,
      "NP Krka - Lozovac entrance": 500,
      "NP Krka - Roški Slap entrance": 500,
      "Skradin - center": 480,
      "Marina ACI Skradin": 500
    },
    "Brodarica - Šibenik": {
      "Split Airport (SPU)": 95,
      "NP Krka - Skradin entrance": 55,
      "NP Krka - Lozovac entrance": 55,
      "NP Krka - Roški Slap entrance": 80,
      "Skradin - center": 55,
      "Marina ACI Skradin": 55
    },
    "Bilice": {
      "Split Airport (SPU)": 100,
      "NP Krka - Skradin entrance": 40,
      "NP Krka - Lozovac entrance": 40,
      "NP Krka - Roški Slap entrance": 80,
      "Skradin - center": 40,
      "Marina ACI Skradin": 40
    },
    "Dubrovnik Airport (DBV)": {
      "Split Airport (SPU)": 450,
      "Šibenik - center": 500,
      "Amadria Park Hotel Šibenik": 500,
      "D-Resort Hotel Šibenik": 500,
      "D-Marin Marina Mandalina Šibenik": 500,
      "NP Krka - Skradin entrance": 500,
      "NP Krka - Lozovac entrance": 500,
      "NP Krka - Roški Slap entrance": 500,
      "Skradin - center": 500,
      "Marina ACI Skradin": 500
    },
    "Zagreb Airport (ZAG)": {
      "Split Airport (SPU)": 550,
      "Šibenik - center": 500,
      "Amadria Park Hotel Šibenik": 500,
      "D-Resort Hotel Šibenik": 500,
      "D-Marin Marina Mandalina Šibenik": 500,
      "NP Krka - Skradin entrance": 500,
      "NP Krka - Lozovac entrance": 500,
      "NP Krka - Roški Slap entrance": 500,
      "Skradin - center": 500,
      "Marina ACI Skradin": 500
    },
    "NP Plitvice Lakes": {
      "Split Airport (SPU)": 395,
      "Šibenik - center": 310,
      "Amadria Park Hotel Šibenik": 310,
      "D-Resort Hotel Šibenik": 310,
      "D-Marin Marina Mandalina Šibenik": 310,
      "NP Krka - Skradin entrance": 290,
      "NP Krka - Lozovac entrance": 310,
      "NP Krka - Roški Slap entrance": 290,
      "Skradin - center": 290,
      "Marina ACI Skradin": 290
    },
    "Skradin - center": {
      "Split Airport (SPU)": 110,
      "Zadar Airport (ZAD)": 105,
      "Šibenik - center": 50,
      "Amadria Park Hotel Šibenik": 50,
      "D-Resort Hotel Šibenik": 50,
      "D-Marin Marina Mandalina Šibenik": 50,
      "Vodice": 60,
      "Tisno": 65,
      "Zadar": 130,
      "Split": 140,
      "Primošten": 80,
      "Srima": 65,
      "NP Krka - Lozovac entrance": 25,
      "NP Krka - Roški Slap entrance": 50,
      "Žaborić": 75,
      "Grebaštica": 80,
      "Zaton": 60,
      "Dubrovnik": 480,
      "Zagreb": 480,
      "Brodarica - Šibenik": 55,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 290,
      "Marina Zaton": 55,
      "Betina": 75,
      "Pirovac": 65,
      "Murter": 75,
      "Bilo": 85,
      "Jadrija": 75,
      "Jezera": 70,
      "Rogoznica": 90,
      "Trogir": 100,
      "Tribunj": 60
    },
    "Marina ACI Skradin": {
      "Split Airport (SPU)": 100,
      "Zadar Airport (ZAD)": 100,
      "Šibenik - center": 50,
      "Amadria Park Hotel Šibenik": 50,
      "D-Resort Hotel Šibenik": 50,
      "D-Marin Marina Mandalina Šibenik": 50,
      "Vodice": 70,
      "Tisno": 90,
      "Zadar": 130,
      "Split": 140,
      "Primošten": 85,
      "Srima": 65,
      "NP Krka - Lozovac entrance": 25,
      "NP Krka - Roški Slap entrance": 50,
      "Žaborić": 75,
      "Grebaštica": 80,
      "Zaton": 60,
      "Dubrovnik": 500,
      "Zagreb": 500,
      "Brodarica - Šibenik": 55,
      "Bilice": 40,
      "Dubrovnik Airport (DBV)": 500,
      "Zagreb Airport (ZAG)": 500,
      "NP Plitvice Lakes": 290,
      "Marina Zaton": 55,
      "Betina": 100,
      "Pirovac": 50,
      "Murter": 100,
      "Bilo": 85,
      "Jadrija": 75,
      "Jezera": 90,
      "Rogoznica": 105,
      "Trogir": 95,
      "Tribunj": 80
    },
    "Marina Zaton": {
      "Split Airport (SPU)": 115,
      "Šibenik - center": 20,
      "Amadria Park Hotel Šibenik": 30,
      "D-Resort Hotel Šibenik": 30,
      "D-Marin Marina Mandalina Šibenik": 30,
      "NP Krka - Skradin entrance": 55,
      "NP Krka - Lozovac entrance": 65,
      "NP Krka - Roški Slap entrance": 75,
      "Skradin - center": 55,
      "Marina ACI Skradin": 55
    },
    "Betina": {
      "Split Airport (SPU)": 150,
      "Šibenik - center": 70,
      "Amadria Park Hotel Šibenik": 80,
      "D-Resort Hotel Šibenik": 70,
      "D-Marin Marina Mandalina Šibenik": 70,
      "NP Krka - Skradin entrance": 75,
      "NP Krka - Lozovac entrance": 85,
      "NP Krka - Roški Slap entrance": 115,
      "Skradin - center": 75,
      "Marina ACI Skradin": 100
    },
    "Pirovac": {
      "Split Airport (SPU)": 125,
      "Šibenik - center": 50,
      "Amadria Park Hotel Šibenik": 55,
      "D-Resort Hotel Šibenik": 50,
      "D-Marin Marina Mandalina Šibenik": 50,
      "NP Krka - Skradin entrance": 65,
      "NP Krka - Lozovac entrance": 80,
      "NP Krka - Roški Slap entrance": 85,
      "Skradin - center": 65,
      "Marina ACI Skradin": 50
    },
    "Murter": {
      "Split Airport (SPU)": 150,
      "Šibenik - center": 70,
      "Amadria Park Hotel Šibenik": 80,
      "D-Resort Hotel Šibenik": 70,
      "D-Marin Marina Mandalina Šibenik": 70,
      "NP Krka - Skradin entrance": 75,
      "NP Krka - Lozovac entrance": 100,
      "NP Krka - Roški Slap entrance": 115,
      "Skradin - center": 75,
      "Marina ACI Skradin": 100
    },
    "Bilo": {
      "Split Airport (SPU)": 80,
      "Šibenik - center": 40,
      "Amadria Park Hotel Šibenik": 40,
      "D-Resort Hotel Šibenik": 40,
      "D-Marin Marina Mandalina Šibenik": 40,
      "NP Krka - Skradin entrance": 85,
      "NP Krka - Lozovac entrance": 80,
      "NP Krka - Roški Slap entrance": 125,
      "Skradin - center": 85,
      "Marina ACI Skradin": 85
    },
    "Jadrija": {
      "Split Airport (SPU)": 115,
      "Šibenik - center": 30,
      "Amadria Park Hotel Šibenik": 40,
      "D-Resort Hotel Šibenik": 40,
      "D-Marin Marina Mandalina Šibenik": 40,
      "NP Krka - Skradin entrance": 75,
      "NP Krka - Lozovac entrance": 70,
      "NP Krka - Roški Slap entrance": 100,
      "Skradin - center": 75,
      "Marina ACI Skradin": 75
    },
    "Jezera": {
      "Split Airport (SPU)": 135,
      "Šibenik - center": 55,
      "Amadria Park Hotel Šibenik": 65,
      "D-Resort Hotel Šibenik": 60,
      "D-Marin Marina Mandalina Šibenik": 60,
      "NP Krka - Skradin entrance": 70,
      "NP Krka - Lozovac entrance": 90,
      "NP Krka - Roški Slap entrance": 95,
      "Skradin - center": 70,
      "Marina ACI Skradin": 90
    },
    "Rogoznica": {
      "Split Airport (SPU)": 80,
      "Šibenik - center": 65,
      "Amadria Park Hotel Šibenik": 65,
      "D-Resort Hotel Šibenik": 65,
      "D-Marin Marina Mandalina Šibenik": 65,
      "NP Krka - Skradin entrance": 90,
      "NP Krka - Lozovac entrance": 95,
      "NP Krka - Roški Slap entrance": 120,
      "Skradin - center": 90,
      "Marina ACI Skradin": 105
    },
    "Trogir": {
      "Šibenik - center": 95,
      "Amadria Park Hotel Šibenik": 95,
      "D-Resort Hotel Šibenik": 95,
      "D-Marin Marina Mandalina Šibenik": 95,
      "NP Krka - Skradin entrance": 100,
      "NP Krka - Lozovac entrance": 95,
      "NP Krka - Roški Slap entrance": 110,
      "Skradin - center": 100,
      "Marina ACI Skradin": 94
    },
    "Tribunj": {
      "Split Airport (SPU)": 120,
      "Šibenik - center": 40,
      "Amadria Park Hotel Šibenik": 45,
      "D-Resort Hotel Šibenik": 40,
      "D-Marin Marina Mandalina Šibenik": 40,
      "NP Krka - Skradin entrance": 60,
      "NP Krka - Lozovac entrance": 70,
      "NP Krka - Roški Slap entrance": 95,
      "Skradin - center": 60,
      "Marina ACI Skradin": 80
    }
  };

  const LOCATIONS = ["Split Airport (SPU)", "Zadar Airport (ZAD)", "Šibenik - center", "Amadria Park Hotel Šibenik", "D-Resort Hotel Šibenik", "D-Marin Marina Mandalina Šibenik", "Vodice", "Tisno", "Zadar", "Split", "Primošten", "Srima", "NP Krka - Skradin entrance", "NP Krka - Lozovac entrance", "NP Krka - Roški Slap entrance", "Žaborić", "Grebaštica", "Zaton", "Dubrovnik", "Zagreb", "Brodarica - Šibenik", "Bilice", "Dubrovnik Airport (DBV)", "Zagreb Airport (ZAG)", "NP Plitvice Lakes", "Skradin - center", "Marina ACI Skradin", "Marina Zaton", "Betina", "Pirovac", "Murter", "Bilo", "Jadrija", "Jezera", "Rogoznica", "Trogir", "Tribunj"];

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

  // Price for one direction; prefers the exact directional value and falls back
  // to the reverse direction when only one is listed. Returns null if the pair
  // has no fixed price (custom quote).
  function priceOneWay(from, to) {
    const f = PRICES[from];
    if (f && f[to] != null) return f[to];
    const r = PRICES[to];
    if (r && r[from] != null) return r[from];
    return null;
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

    const oneway = priceOneWay(from, to);
    if (oneway != null) {
      let total, sub;
      if (tripType === 'return') {
        total = oneway + priceOneWay(to, from);
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
