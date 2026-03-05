/* ============================================================
   SAMOTICS RESOURCES HUB — JavaScript
   Paste into Bricks Custom Code (Footer)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
  // Animate cards on scroll
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

  // Animate type cards
  const typeCards = document.querySelectorAll('.sam-resources__type-card');
  typeCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Animate featured cards
  const featuredCards = document.querySelectorAll('.sam-resources__featured-card');
  featuredCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 100}ms, transform 600ms ease-out ${index * 100}ms`;
    observer.observe(card);
  });

  // Newsletter form submission
  const newsletterForm = document.querySelector('.sam-resources__newsletter-form');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', function(e) {
      e.preventDefault();
      const emailInput = this.querySelector('#newsletter-email');
      if (emailInput.value) {
        alert('Thank you for subscribing! Check your email to confirm.');
        emailInput.value = '';
      }
    });
  }
});
