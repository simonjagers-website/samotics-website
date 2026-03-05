/* ============================================================
   SAMOTICS FOOTER — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Footer Accordion (mobile only) ── */
  var cols = document.querySelectorAll('[data-footer-accordion]');
  if (!cols.length) return;

  function isMobile() {
    return window.innerWidth <= 991;
  }

  cols.forEach(function (col) {
    var heading = col.querySelector('.sam-footer__col-heading');
    if (!heading) return;

    heading.addEventListener('click', function () {
      if (!isMobile()) return;

      var isOpen = col.classList.contains('is-open');

      // Close all other columns
      cols.forEach(function (c) {
        if (c !== col) c.classList.remove('is-open');
      });

      // Toggle current
      col.classList.toggle('is-open');
    });
  });

  /* ── Reset accordion state on resize to desktop ── */
  var mql = window.matchMedia('(min-width: 992px)');

  function handleResize(e) {
    if (e.matches) {
      cols.forEach(function (col) {
        col.classList.remove('is-open');
      });
    }
  }

  if (mql.addEventListener) {
    mql.addEventListener('change', handleResize);
  } else {
    mql.addListener(handleResize);
  }

})();