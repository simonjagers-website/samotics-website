/* ============================================================
   SAMOTICS CHEMICALS PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  var main = document.getElementById('main-content');
  if (main && !main.getAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
})();
