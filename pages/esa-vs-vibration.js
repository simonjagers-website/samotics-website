/* ============================================================
   SAMOTICS ESA VS VIBRATION PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* Ensure skip-link target exists */
  var main = document.getElementById('main-content');
  if (main) main.setAttribute('tabindex', '-1');

  /* Smooth scroll for any in-page anchor links */
  document.querySelectorAll('.sam-versus a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        var offset = 80 + 24; /* sticky nav height + breathing room */
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
        target.focus({ preventScroll: true });
      }
    });
  });
})();
