/* ============================================================
   SAMOTICS CASE STUDY TEMPLATE — JavaScript
   Paste into Bricks Template → JS tab
   ============================================================ */
(function () {
  'use strict';

  /* ── KPI count-up animation on scroll ── */
  var kpiSection = document.querySelector('.sam-case-kpis');
  if (!kpiSection) return;

  var values = kpiSection.querySelectorAll('.kpi-value');
  var animated = false;

  function animateKPIs() {
    if (animated) return;
    animated = true;

    values.forEach(function (el) {
      var raw = el.getAttribute('data-target') || el.textContent;
      // Extract numeric part: "£748K" → 748, "637" → 637, "800%" → 800
      var match = raw.match(/([\d,.]+)/);
      if (!match) return;

      var target = parseFloat(match[1].replace(/,/g, ''));
      var prefix = raw.substring(0, raw.indexOf(match[1]));
      var suffix = raw.substring(raw.indexOf(match[1]) + match[1].length);
      var duration = 1200;
      var start = performance.now();

      function step(now) {
        var progress = Math.min((now - start) / duration, 1);
        // Ease-out cubic
        var eased = 1 - Math.pow(1 - progress, 3);
        var current = Math.round(target * eased);

        // Format with commas if original had them
        var formatted = match[1].indexOf(',') > -1
          ? current.toLocaleString()
          : String(current);

        el.textContent = prefix + formatted + suffix;

        if (progress < 1) requestAnimationFrame(step);
      }

      requestAnimationFrame(step);
    });
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animateKPIs();
        observer.disconnect();
      }
    });
  }, { threshold: 0.3 });

  observer.observe(kpiSection);
})();
