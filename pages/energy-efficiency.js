/* ============================================================
   SAMOTICS ENERGY EFFICIENCY PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.getAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  /* ── Smooth scroll for same-page links ── */
  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var target = document.querySelector(a.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();
