/* ============================================================
   SAMOTICS HEADER — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  var header = document.querySelector('.sam-header');
  if (!header) return;

  /* ── Scroll: toggle .is-scrolled ── */
  var scrollThreshold = 20;

  function onScroll() {
    if (window.scrollY > scrollThreshold) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll(); // initial check

  /* ── Mobile Menu Toggle ── */
  var hamburger = header.querySelector('.sam-hamburger');
  var mobileMenu = document.getElementById('sam-mobile-menu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', function () {
      var isOpen = hamburger.getAttribute('aria-expanded') === 'true';
      hamburger.setAttribute('aria-expanded', String(!isOpen));
      hamburger.setAttribute('aria-label', isOpen ? 'Open menu' : 'Close menu');
      mobileMenu.classList.toggle('is-open');
      mobileMenu.setAttribute('aria-hidden', String(isOpen));
      document.body.style.overflow = isOpen ? '' : 'hidden';
    });
  }

  /* ── Mobile Accordion Toggles ── */
  var toggles = header.querySelectorAll('.sam-mobile-nav__toggle');
  toggles.forEach(function (toggle) {
    toggle.addEventListener('click', function () {
      var group = this.closest('.sam-mobile-nav__group');
      var isOpen = group.classList.contains('is-open');

      // Close all others
      header.querySelectorAll('.sam-mobile-nav__group.is-open').forEach(function (g) {
        if (g !== group) {
          g.classList.remove('is-open');
          g.querySelector('.sam-mobile-nav__toggle').setAttribute('aria-expanded', 'false');
        }
      });

      // Toggle current
      group.classList.toggle('is-open');
      this.setAttribute('aria-expanded', String(!isOpen));
    });
  });

  /* ── Desktop Dropdown Keyboard Navigation ── */
  var dropdownTriggers = header.querySelectorAll('.sam-nav__link--dropdown');
  dropdownTriggers.forEach(function (trigger) {
    var parent = trigger.closest('.sam-nav__item--has-dropdown');
    var dropdown = parent.querySelector('.sam-dropdown');
    var items = dropdown ? dropdown.querySelectorAll('.sam-dropdown__item') : [];

    trigger.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        var expanded = trigger.getAttribute('aria-expanded') === 'true';
        trigger.setAttribute('aria-expanded', String(!expanded));

        if (!expanded && items.length) {
          items[0].focus();
        }
      }

      if (e.key === 'ArrowDown' && items.length) {
        e.preventDefault();
        trigger.setAttribute('aria-expanded', 'true');
        items[0].focus();
      }

      if (e.key === 'Escape') {
        trigger.setAttribute('aria-expanded', 'false');
        trigger.focus();
      }
    });

    // Arrow navigation within dropdown
    items.forEach(function (item, index) {
      item.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (index < items.length - 1) items[index + 1].focus();
        }
        if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (index > 0) {
            items[index - 1].focus();
          } else {
            trigger.focus();
          }
        }
        if (e.key === 'Escape') {
          trigger.setAttribute('aria-expanded', 'false');
          trigger.focus();
        }
        if (e.key === 'Tab' && !e.shiftKey && index === items.length - 1) {
          trigger.setAttribute('aria-expanded', 'false');
        }
      });
    });
  });

  /* ── Close mobile menu on resize to desktop ── */
  var mql = window.matchMedia('(min-width: 992px)');
  function handleResize(e) {
    if (e.matches && mobileMenu && mobileMenu.classList.contains('is-open')) {
      hamburger.setAttribute('aria-expanded', 'false');
      hamburger.setAttribute('aria-label', 'Open menu');
      mobileMenu.classList.remove('is-open');
      mobileMenu.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }
  }
  if (mql.addEventListener) {
    mql.addEventListener('change', handleResize);
  } else {
    mql.addListener(handleResize);
  }

  /* ── Close dropdown on outside click (desktop) ── */
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.sam-nav__item--has-dropdown')) {
      dropdownTriggers.forEach(function (t) {
        t.setAttribute('aria-expanded', 'false');
      });
    }
  });

})();