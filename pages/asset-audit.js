/* ============================================================
   SAMOTICS ASSET AUDIT PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.getAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  /* ── Elements ── */
  var form         = document.getElementById('audit-form');
  var confirmation = document.getElementById('audit-confirmation');
  var confHeading  = document.getElementById('confirmation-heading');
  if (!form) return;

  /* ── Free-email domains ── */
  var freeEmails = ['gmail.com','hotmail.com','yahoo.com','outlook.com','live.com','aol.com','icloud.com'];

  /* ── Helpers ── */
  function getField(name) {
    return form.querySelector('[name="' + name + '"]');
  }

  function showHint(emailField) {
    var hint = emailField.closest('.sam-audit-form__field').querySelector('.sam-audit-form__hint');
    if (!hint) return;
    var domain = (emailField.value.split('@')[1] || '').toLowerCase();
    hint.hidden = !freeEmails.includes(domain);
  }

  function validateField(field) {
    var wrapper = field.closest('.sam-audit-form__field');
    if (!wrapper) return true;
    var valid = field.checkValidity();
    wrapper.classList.toggle('sam-audit-form__field--error', !valid);
    return valid;
  }

  /* ── Inline validation on blur ── */
  form.querySelectorAll('input, select, textarea').forEach(function (el) {
    el.addEventListener('blur', function () {
      validateField(this);
      if (this.type === 'email') showHint(this);
    });
  });

  /* ── Submission ── */
  form.addEventListener('submit', function (e) {
    e.preventDefault();

    /* Honeypot check */
    var hp = getField('website');
    if (hp && hp.value) return;

    /* Validate all required fields */
    var allValid = true;
    form.querySelectorAll('[required]').forEach(function (el) {
      if (!validateField(el)) allValid = false;
    });
    if (!allValid) return;

    /* GDPR check */
    var consent = form.querySelector('[name="gdpr_consent"]');
    if (consent && !consent.checked) {
      var wrapper = consent.closest('.sam-audit-form__consent');
      if (wrapper) wrapper.style.outline = '2px solid #C4314B';
      return;
    }

    /* Loading state */
    var btn = form.querySelector('.sam-audit-form__submit');
    var originalText = btn.textContent;
    btn.textContent = 'Sending...';
    btn.disabled = true;

    /* Collect data */
    var data = {};
    new FormData(form).forEach(function (val, key) { data[key] = val; });

    /* GTM data layer push */
    if (typeof window.dataLayer !== 'undefined') {
      window.dataLayer.push({
        event: 'form_submission',
        form_type: 'asset_audit',
        source_page: window.location.pathname,
        industry: data.industry || '',
        fleet_size: data.rotating_assets || ''
      });
    }

    /* Simulate network delay, then show confirmation */
    setTimeout(function () {
      var firstName = data.first_name || '';
      if (confHeading && firstName) {
        confHeading.textContent = 'Thanks, ' + firstName + '. We\'ll prepare your asset audit scope.';
      }
      form.hidden = true;
      confirmation.hidden = false;
      confirmation.scrollIntoView({ behavior: 'smooth', block: 'start' });

      /* Reset button for potential back-navigation */
      btn.textContent = originalText;
      btn.disabled = false;
    }, 800);
  });

})();
