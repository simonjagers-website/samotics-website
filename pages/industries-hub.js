/* ============================================================
   SAMOTICS INDUSTRIES HUB — JavaScript
   Paste into Bricks Custom Code (Footer)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
  // Animate stats on scroll
  const observerOptions = {
    threshold: 0.2,
    rootMargin: '0px 0px -100px 0px'
  };

  const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Animate stat numbers
        if (entry.target.classList.contains('sam-industries__stat-number')) {
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        }

        // Animate cards
        if (entry.target.classList.contains('sam-industries__industry-card') ||
            entry.target.classList.contains('sam-industries__value-card')) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      }
    });
  }, observerOptions);

  // Observe stat numbers
  const statNumbers = document.querySelectorAll('.sam-industries__stat-number');
  statNumbers.forEach(stat => {
    stat.style.opacity = '0';
    observer.observe(stat);
  });

  // Observe industry cards
  const industryCards = document.querySelectorAll('.sam-industries__industry-card');
  industryCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Observe value cards
  const valueCards = document.querySelectorAll('.sam-industries__value-card');
  valueCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Counter animation function
  function animateCounter(element) {
    const text = element.textContent;
    const numMatch = text.match(/(\d+)/);
    if (!numMatch) return;

    const target = parseInt(numMatch[1]);
    const suffix = text.replace(/\d+/, '');
    const duration = 1500;
    const start = Date.now();

    function update() {
      const elapsed = Date.now() - start;
      const progress = Math.min(elapsed / duration, 1);
      const current = Math.floor(progress * target);
      element.textContent = current + suffix;

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    update();
  }
});
