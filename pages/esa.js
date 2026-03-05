/* ============================================================
   SAMOTICS ESA TECHNOLOGY PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Accessible: skip-to-content ── */
  var main = document.getElementById('main-content');
  if (main) main.setAttribute('tabindex', '-1');

  /* ── Smooth anchor scrolling for jump nav ── */
  document.querySelectorAll('.sam-esa a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        /* Account for sticky nav height (80px) */
        var offset = 80 + 24;
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
        target.focus({ preventScroll: true });
      }
    });
  });

})();
