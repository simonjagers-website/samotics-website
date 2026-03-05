/* ============================================================
   SAMOTICS WEBINAR POST TEMPLATE — JavaScript
   Paste into Bricks Template → JS tab
   ============================================================ */
(function () {
  'use strict';

  /* ── Smooth scroll to video if URL contains #watch ── */
  if (window.location.hash === '#watch') {
    var media = document.querySelector('.sam-webinar-media');
    if (media) {
      media.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
  }
})();
