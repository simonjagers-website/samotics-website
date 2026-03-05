/* ============================================================
   SAMOTICS HOW IT INSTALLS PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.hasAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }
})();
