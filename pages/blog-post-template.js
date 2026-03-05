/* ============================================================
   SAMOTICS BLOG POST TEMPLATE — JavaScript
   Paste into Bricks Template → JS tab
   ============================================================ */
(function () {
  'use strict';

  /* ── Auto-generate Table of Contents from h2 headings ── */
  var tocNav  = document.getElementById('toc-nav');
  var content = document.querySelector('.sam-post-body__content');
  if (!tocNav || !content) return;

  var headings = content.querySelectorAll('h2');
  if (headings.length < 2) {
    // Hide TOC if fewer than 2 headings
    var tocBlock = document.querySelector('.sam-post-body__toc');
    if (tocBlock) tocBlock.style.display = 'none';
    return;
  }

  headings.forEach(function (h2, i) {
    // Create anchor ID
    var id = h2.id || 'section-' + (i + 1);
    h2.id = id;

    // Create TOC link
    var link = document.createElement('a');
    link.href = '#' + id;
    link.textContent = h2.textContent;
    tocNav.appendChild(link);
  });

  /* ── Highlight active TOC link on scroll ── */
  var tocLinks = tocNav.querySelectorAll('a');
  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        tocLinks.forEach(function (l) { l.classList.remove('active'); });
        var active = tocNav.querySelector('a[href="#' + entry.target.id + '"]');
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-80px 0px -60% 0px', threshold: 0 });

  headings.forEach(function (h2) { observer.observe(h2); });

  /* ── Smooth scroll on TOC click ── */
  tocNav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      e.preventDefault();
      var target = document.querySelector(e.target.getAttribute('href'));
      if (target) {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        history.replaceState(null, '', e.target.getAttribute('href'));
      }
    }
  });
})();
