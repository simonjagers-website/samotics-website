/* ============================================================
   SAMOTICS PROOF HUB PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.hasAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  /* ── Card collections ── */
  var caseCards   = document.querySelectorAll('#proof-cards .sam-proof-card');
  var detectCards = document.querySelectorAll('#detect-cards .sam-proof-card');
  var filterBtns  = document.querySelectorAll('.sam-proof-grid__filter-btn');

  /* Empty-state elements */
  var caseEmpty   = document.getElementById('proof-empty');
  var detectEmpty = document.getElementById('detect-empty');

  /* Reset buttons (inside empty states) */
  var caseReset   = document.getElementById('proof-reset');
  var detectReset = document.getElementById('detect-reset');

  /* Active filters state */
  var activeFilters = {
    industry: 'all',
    outcome:  'all'
  };

  /* ── Filter a set of cards, return visible count ── */
  function filterCards(cards) {
    var visible = 0;
    cards.forEach(function (card) {
      var industryMatch = activeFilters.industry === 'all' ||
        card.getAttribute('data-industry') === activeFilters.industry;
      var outcomeMatch = activeFilters.outcome === 'all' ||
        card.getAttribute('data-outcome').indexOf(activeFilters.outcome) !== -1;
      var show = industryMatch && outcomeMatch;
      card.hidden = !show;
      if (show) visible++;
    });
    return visible;
  }

  /* ── Apply filters to both grids ── */
  function applyFilters() {
    var caseVisible   = filterCards(caseCards);
    var detectVisible = filterCards(detectCards);

    if (caseEmpty)   caseEmpty.hidden   = caseVisible > 0;
    if (detectEmpty) detectEmpty.hidden = detectVisible > 0;
  }

  /* ── Button click handler ── */
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var filterType  = this.getAttribute('data-filter');
      var filterValue = this.getAttribute('data-value');

      activeFilters[filterType] = filterValue;

      /* Update active class within the same group */
      document.querySelectorAll('[data-filter="' + filterType + '"]').forEach(function (b) {
        b.classList.remove('sam-proof-grid__filter-btn--active');
      });
      this.classList.add('sam-proof-grid__filter-btn--active');

      applyFilters();
    });
  });

  /* ── Reset helper ── */
  function resetFilters() {
    activeFilters.industry = 'all';
    activeFilters.outcome  = 'all';
    filterBtns.forEach(function (btn) {
      btn.classList.remove('sam-proof-grid__filter-btn--active');
      if (btn.getAttribute('data-value') === 'all') {
        btn.classList.add('sam-proof-grid__filter-btn--active');
      }
    });
    applyFilters();
  }

  if (caseReset)   caseReset.addEventListener('click', resetFilters);
  if (detectReset) detectReset.addEventListener('click', resetFilters);

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
})();
