/* ============================================================
   SAMOTICS SECURITY & COMPLIANCE PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.hasAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  /* ── Smooth scroll for in-page anchors ── */
  var headerH = 80;
  var gap     = 24;
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var id = this.getAttribute('href').slice(1);
      var target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      var top = target.getBoundingClientRect().top + window.pageYOffset - headerH - gap;
      window.scrollTo({ top: top, behavior: 'smooth' });
      target.setAttribute('tabindex', '-1');
      target.focus({ preventScroll: true });
    });
  });

  /* ── "All of the above" checkbox logic ── */
  var allCheckbox = document.querySelector('input[value="all"]');
  var docCheckboxes = document.querySelectorAll('input[name="docs"]:not([value="all"])');
  if (allCheckbox && docCheckboxes.length) {
    allCheckbox.addEventListener('change', function () {
      docCheckboxes.forEach(function (cb) { cb.checked = allCheckbox.checked; });
    });
    docCheckboxes.forEach(function (cb) {
      cb.addEventListener('change', function () {
        allCheckbox.checked = Array.from(docCheckboxes).every(function (c) { return c.checked; });
      });
    });
  }
})();
