/*
  404 Page JavaScript
  Paste this into the Bricks Code element JS tab
  Handles search form submission and back button
*/

document.addEventListener('DOMContentLoaded', function() {
  // Search form
  const searchForm = document.getElementById('search-form');
  const searchInput = document.getElementById('search-input');
  const backButton = document.getElementById('back-button');

  // Handle search form submission
  if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
      e.preventDefault();

      const query = searchInput.value.trim();

      if (query.length > 0) {
        // Redirect to WordPress site search
        window.location.href = '/?s=' + encodeURIComponent(query);
      }
    });
  }

  // Handle back button click
  if (backButton) {
    backButton.addEventListener('click', function() {
      // Go back in browser history
      window.history.back();
    });
  }

  // Auto-focus search input
  if (searchInput) {
    searchInput.focus();
  }

  // Allow Enter key to trigger search from anywhere
  document.addEventListener('keypress', function(e) {
    if (e.key === 'Enter' && document.activeElement === searchInput) {
      searchForm.dispatchEvent(new Event('submit'));
    }
  });
});
