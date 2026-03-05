/* ============================================================
   SAMOTICS INDUSTRY PAGE — JavaScript
   Paste into Bricks Code Element → JS tab
   ============================================================ */

document.addEventListener("DOMContentLoaded", function () {
  /* ── Animate stats on scroll ── */
  const stats = document.querySelectorAll(".sam-ind-results__stat-value");
  if (stats.length === 0) return;

  const observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        if (el.dataset.animated) return;
        el.dataset.animated = "true";

        const raw = el.textContent.trim();
        // Extract numeric part
        const match = raw.match(/^([^\d]*)([\d,.]+)(.*)$/);
        if (!match) return;

        const prefix = match[1];
        const numStr = match[2].replace(/,/g, "");
        const suffix = match[3];
        const target = parseFloat(numStr);
        const hasDecimal = numStr.includes(".");
        const decimals = hasDecimal ? numStr.split(".")[1].length : 0;
        const hasComma = match[2].includes(",");
        const duration = 1200;
        const start = performance.now();

        function tick(now) {
          const elapsed = now - start;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          let current = target * eased;
          let formatted;
          if (hasDecimal) {
            formatted = current.toFixed(decimals);
          } else {
            formatted = Math.round(current).toString();
          }
          if (hasComma) {
            formatted = formatted.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
          }
          el.textContent = prefix + formatted + suffix;
          if (progress < 1) requestAnimationFrame(tick);
        }

        el.textContent = prefix + "0" + suffix;
        requestAnimationFrame(tick);
      });
    },
    { threshold: 0.3 }
  );

  stats.forEach(function (el) {
    observer.observe(el);
  });
});
