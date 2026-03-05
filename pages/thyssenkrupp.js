// ============================================================
// SAMOTICS PROOF PAGE - INTERACTIVITY
// ArcelorMittal (thyssenkrupp.html)
// ============================================================

// Counter Animation for KPI and Results Values
function animateCounters() {
  const counters = document.querySelectorAll('[data-counter]');

  const observerOptions = {
    threshold: 0.3
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !entry.target.classList.contains('counted')) {
        const target = entry.target;
        const finalValue = parseInt(target.dataset.counter);
        const displayText = target.textContent;
        const prefix = displayText.replace(/[0-9]/g, '').trim();
        const suffix = displayText.match(/[a-zA-Z/mo]*$/)?.[0] || '';

        let currentValue = 0;
        const increment = Math.ceil(finalValue / 30);

        const counter = setInterval(() => {
          currentValue += increment;
          if (currentValue >= finalValue) {
            currentValue = finalValue;
            clearInterval(counter);
            target.classList.add('counted');
          }
          target.textContent = prefix + currentValue + suffix;
        }, 30);

        observer.unobserve(target);
      }
    });
  }, observerOptions);

  counters.forEach(counter => observer.observe(counter));
}

// Stagger Animation for Cards
function staggerAnimateCards() {
  const cards = document.querySelectorAll('.sam-proof-results__card, .sam-proof-related__card');

  const observerOptions = {
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
        setTimeout(() => {
          entry.target.style.animation = 'slideUp 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) forwards';
          entry.target.classList.add('animated');
        }, index * 100);
      }
    });
  }, observerOptions);

  cards.forEach(card => observer.observe(card));
}

// Add CSS animation keyframes dynamically
function addAnimationStyles() {
  const style = document.createElement('style');
  style.textContent = `
    @keyframes slideUp {
      from {
        opacity: 0;
        transform: translateY(30px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    .sam-proof-results__card,
    .sam-proof-related__card {
      opacity: 0;
    }

    @media (prefers-reduced-motion: reduce) {
      @keyframes slideUp {
        from {
          opacity: 1;
          transform: translateY(0);
        }
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
    }
  `;
  document.head.appendChild(style);
}

// Smooth scroll for anchor links
function setupSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);

      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', () => {
  addAnimationStyles();
  animateCounters();
  staggerAnimateCards();
  setupSmoothScroll();
});
