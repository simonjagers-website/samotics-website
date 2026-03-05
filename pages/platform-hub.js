/* ============================================================
   SAMOTICS PLATFORM HUB — JavaScript
   Paste into Bricks Custom Code (Footer)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
  // Smooth scroll to sections
  const navLinks = document.querySelectorAll('.sam-platform__hero-nav a');

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

  // Animate elements on scroll
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

  // Animate pillar cards
  const pillarCards = document.querySelectorAll('.sam-platform__pillar-card');
  pillarCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Animate flow steps
  const flowSteps = document.querySelectorAll('.sam-platform__flow-step');
  flowSteps.forEach((step, index) => {
    step.style.opacity = '0';
    step.style.transform = 'translateY(20px)';
    step.style.transition = `opacity 600ms ease-out ${index * 150}ms, transform 600ms ease-out ${index * 150}ms`;
    observer.observe(step);
  });

  // Animate capability cards
  const capabilityCards = document.querySelectorAll('.sam-platform__capability-card');
  capabilityCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Animate subnav cards
  const subnavCards = document.querySelectorAll('.sam-platform__subnav-card');
  subnavCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });
});
