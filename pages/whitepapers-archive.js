/* ============================================================
   WHITEPAPERS HUB — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function() {
  const modal = document.getElementById('sam-wp-modal');
  const form = document.getElementById('sam-wp-form');
  const wpIdInput = document.getElementById('sam-wp-id');
  const closeBtn = modal?.querySelector('.sam-wp-modal__close');
  const backdrop = modal?.querySelector('.sam-wp-modal__backdrop');

  if (!modal) return;

  // Open modal when any download button is clicked
  document.querySelectorAll('.sam-wp-card__cta').forEach(function(btn) {
    btn.addEventListener('click', function() {
      var wpId = this.getAttribute('data-wp-id');
      if (wpIdInput) wpIdInput.value = wpId;
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      // Focus first input
      setTimeout(function() {
        var firstInput = modal.querySelector('.sam-wp-modal__input');
        if (firstInput) firstInput.focus();
      }, 100);
    });
  });

  // Close modal
  function closeModal() {
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (backdrop) backdrop.addEventListener('click', closeModal);

  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && modal.getAttribute('aria-hidden') === 'false') {
      closeModal();
    }
  });

  // Form submit placeholder
  // REPLACE THIS with your HubSpot/WPForms integration
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var wpId = wpIdInput ? wpIdInput.value : '';
      var email = form.querySelector('[name="email"]').value;
      var name = form.querySelector('[name="name"]').value;

      // Placeholder: log the submission
      console.log('Whitepaper download request:', { wpId: wpId, name: name, email: email });

      // Show success state
      var panel = modal.querySelector('.sam-wp-modal__panel');
      if (panel) {
        panel.innerHTML = '<div style="text-align:center;padding:32px 0;">' +
          '<svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#FF5429" stroke-width="2" style="margin-bottom:16px;">' +
          '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/>' +
          '</svg>' +
          '<h3 style="font:600 1.25rem/1.3 var(--sam-font);color:var(--sam-space-cadet);margin:0 0 8px;">Check your email</h3>' +
          '<p style="font:400 1rem/1.5 var(--sam-font);color:var(--sam-comet);margin:0;">We\'ve sent the PDF to <strong>' + email + '</strong></p>' +
          '</div>';
      }

      // Close after 3 seconds
      setTimeout(closeModal, 3000);
    });
  }
})();
