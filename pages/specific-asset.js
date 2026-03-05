/* ============================================================
   SAMOTICS SPECIFIC ASSET PAGE TEMPLATE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

document.addEventListener('DOMContentLoaded', function () {

  /* ── Smooth scroll for anchor links ── */
  document.querySelectorAll('.sam-spec a[href^="#"]').forEach(function (link) {
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
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var sections = document.querySelectorAll(
      '.sam-spec-why, .sam-spec-faults, .sam-spec-stories, ' +
      '.sam-spec-install, .sam-spec-energy, .sam-spec-industries, ' +
      '.sam-spec-related, .sam-cta-block--spec'
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

});
