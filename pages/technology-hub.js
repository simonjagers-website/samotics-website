/* ============================================================
   SAMOTICS TECHNOLOGY HUB — JavaScript
   Paste into Bricks Custom Code (Footer)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
  // Smooth scroll to sections when clicking nav links
  const navLinks = document.querySelectorAll('.sam-technology__hero-nav a');

  navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      const href = this.getAttribute('href');
      if (href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }
    });
  });

  // Add animation to detect cards on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe detect cards
  const detectCards = document.querySelectorAll('.sam-technology__detect-card');
  detectCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Observe subnav cards
  const subnavCards = document.querySelectorAll('.sam-technology__subnav-card');
  subnavCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });
});
