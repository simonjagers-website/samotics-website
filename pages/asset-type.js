/* ============================================================
   SAMOTICS ASSET TYPE PAGE TEMPLATE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── Smooth scroll for anchor links ── */
  document.querySelectorAll('.sam-asset a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        var offset = document.querySelector('.sam-header')
          ? document.querySelector('.sam-header').offsetHeight + 24
          : 80;
        var top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    });
  });

  /* ── Intersection Observer: fade in sections ── */
  if ('IntersectionObserver' in window) {
    var sections = document.querySelectorAll(
      '.sam-asset-subtypes, .sam-asset-faults, .sam-asset-how, ' +
      '.sam-asset-stories, .sam-asset-proof, .sam-asset-industries, ' +
      '.sam-asset-related, .sam-cta-block--asset'
    );

    sections.forEach(function (s) {
      s.style.opacity = '0';
      s.style.transform = 'translateY(24px)';
      s.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08 });

    sections.forEach(function (s) { observer.observe(s); });
  }

  /* ── Respect reduced motion ── */
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.sam-asset section').forEach(function (s) {
      s.style.opacity = '1';
      s.style.transform = 'none';
      s.style.transition = 'none';
    });
  }

});
