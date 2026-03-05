/* ============================================================
   SAMOTICS CASE STUDY TEMPLATE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.getAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  /* ── Smooth scroll for in-page anchors ── */
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  /* ── Track PDF downloads ── */
  document.querySelectorAll('a[href$=".pdf"]').forEach(function (link) {
    link.addEventListener('click', function () {
      if (typeof window.dataLayer !== 'undefined') {
        /* Extract case study name from URL path */
        var caseName = window.location.pathname.split('/').pop() || 'unknown';
        window.dataLayer.push({
          event: 'case_study_download',
          case_study: caseName,
          source_page: window.location.pathname
        });
      }
    });
  });
})();
