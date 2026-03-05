/* ============================================================
   SAMOTICS HOMEPAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  var home = document.querySelector('.sam-home');
  if (!home) return;

  /* ── Fade-In on Scroll (IntersectionObserver) ── */
  var fadeEls = home.querySelectorAll(
    '.sam-solution, .sam-industries, .sam-proof, .sam-platform, .sam-trust, .sam-cta-block'
  );

  if ('IntersectionObserver' in window) {
    var fadeObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            fadeObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: '0px 0px -40px 0px' }
    );

    fadeEls.forEach(function (el) {
      el.classList.add('sam-fade-target');
      fadeObserver.observe(el);
    });

    // Inject fade CSS once
    var style = document.createElement('style');
    style.textContent =
      '.sam-fade-target { opacity: 0; transform: translateY(24px); transition: opacity 0.5s ease-out, transform 0.5s ease-out; }' +
      '.sam-fade-target.is-visible { opacity: 1; transform: translateY(0); }' +
      '@media (prefers-reduced-motion: reduce) { .sam-fade-target { opacity: 1 !important; transform: none !important; transition: none !important; } }';
    document.head.appendChild(style);
  }

  /* ── KPI Counter Animation ── */
  var kpiEls = home.querySelectorAll('.kpi-value[data-count]');

  if (kpiEls.length && 'IntersectionObserver' in window) {
    var kpiObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCount(entry.target);
            kpiObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    kpiEls.forEach(function (el) {
      kpiObserver.observe(el);
    });
  }

  function animateCount(el) {
    var target = parseInt(el.getAttribute('data-count'), 10);
    if (isNaN(target)) return;

    var suffix = '';
    var text = el.textContent.trim();
    if (text.indexOf('+') !== -1) suffix = '+';

    // Determine if we need comma formatting
    var useComma = target >= 1000;
    var duration = 1200;
    var steps = 40;
    var increment = target / steps;
    var current = 0;
    var step = 0;

    var interval = setInterval(function () {
      step++;
      current = Math.min(Math.round(increment * step), target);

      if (useComma) {
        el.textContent = current.toLocaleString('en-US') + suffix;
      } else {
        el.textContent = current + suffix;
      }

      if (step >= steps) {
        clearInterval(interval);
      }
    }, duration / steps);
  }

  /* ── Smooth Scroll for Anchor Links ── */
  home.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

})();