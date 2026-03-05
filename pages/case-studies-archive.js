/* ============================================================
   SAMOTICS CASE STUDIES ARCHIVE — JavaScript
   Paste into Bricks Custom Code (Footer)
   ============================================================ */

document.addEventListener('DOMContentLoaded', function() {
  // Filter functionality
  const filterChips = document.querySelectorAll('.sam-case-studies__filter-chip');
  const caseCards = document.querySelectorAll('.sam-case-studies__card');

  filterChips.forEach(chip => {
    chip.addEventListener('click', function(e) {
      e.preventDefault();

      // Update active state
      filterChips.forEach(c => c.classList.remove('sam-case-studies__filter-chip--active'));
      this.classList.add('sam-case-studies__filter-chip--active');

      // Get filter value from data attribute
      const filter = this.getAttribute('data-filter');

      // Filter cards with animation
      caseCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(10px)';

        setTimeout(() => {
          if (filter === 'all') {
            card.style.display = 'flex';
          } else {
            // Check if card contains the filter category in its tag
            const tag = card.querySelector('.sam-case-studies__card-tag');
            if (tag && tag.textContent.toLowerCase().includes(filter.replace('-', ' '))) {
              card.style.display = 'flex';
            } else {
              card.style.display = 'none';
            }
          }

          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
          card.style.transition = 'opacity 300ms ease-out, transform 300ms ease-out';
        }, 100);
      });

      // Navigate to filtered URL
      const url = this.getAttribute('href');
      if (url && history.pushState) {
        history.pushState(null, null, url);
      }
    });
  });

  // Animate cards on page load
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
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

  caseCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    card.style.transition = `opacity 600ms ease-out ${index * 50}ms, transform 600ms ease-out ${index * 50}ms`;
    observer.observe(card);
  });

  // Handle pagination links
  const paginationLinks = document.querySelectorAll('.sam-case-studies__pagination-link');
  paginationLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      // Allow default navigation (WordPress pagination)
      // or implement AJAX loading if needed
    });
  });
});
