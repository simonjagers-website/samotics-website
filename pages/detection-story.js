/* ============================================================
   SAMOTICS DETECTION STORY — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

/* ── Skip-link target ── */
(function () {
  'use strict';
  var main = document.getElementById('main-content');
  if (main && !main.getAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }
})();
