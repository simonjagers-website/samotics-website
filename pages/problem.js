/* ============================================================
   SAMOTICS PROBLEM PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Accessible: skip-to-content ── */
  var main = document.getElementById('main-content');
  if (main) main.setAttribute('tabindex', '-1');

  /* ── Smooth anchor scrolling (for any in-page links) ── */
  document.querySelectorAll('.sam-problem a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        target.focus({ preventScroll: true });
      }
    });
  });

})();
