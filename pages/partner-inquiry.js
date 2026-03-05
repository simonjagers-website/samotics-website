/* ============================================================
   SAMOTICS PARTNER INQUIRY PAGE — JavaScript
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
  var form         = document.getElementById('partner-form');
  var confirmation = document.getElementById('partner-confirmation');
  var confHeading  = document.getElementById('confirmation-heading');
  if (!form) return;

  /* ── Free-email domains ── */
  var freeEmails = ['gmail.com','hotmail.com','yahoo.com','outlook.com','live.com','aol.com','icloud.com'];

  /* ── Helpers ── */
  function getField(name) {
    return form.querySelector('[name="' + name + '"]');
  }

  function showHint(emailField) {
    var hint = emailField.closest('.sam-pinquiry-form__field').querySelector('.sam-pinquiry-form__hint');
    if (!hint) return;
    var domain = (emailField.value.split('@')[1] || '').toLowerCase();
    hint.hidden = !freeEmails.includes(domain);
  }

  function validateField(field) {
    var wrapper = field.closest('.sam-pinquiry-form__field');
    if (!wrapper) return true;
    var valid = field.checkValidity();
    wrapper.classList.toggle('sam-pinquiry-form__field--error', !valid);
    return valid;
  }

  function validateIndustries() {
    var checked = form.querySelectorAll('input[name="industries"]:checked');
    return checked.length > 0;
  }

  /* ── Inline validation on blur ── */
  form.querySelectorAll('input[type="text"], input[type="email"], select, textarea').forEach(function (el) {
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
      if (el.type === 'checkbox' && el.name === 'gdpr_consent') return; /* handled separately */
      if (!validateField(el)) allValid = false;
    });

    /* Validate industries multi-select */
    if (!validateIndustries()) {
      allValid = false;
      var fieldset = form.querySelector('.sam-pinquiry-form__fieldset');
      if (fieldset) fieldset.style.outline = '2px solid #C4314B';
    } else {
      var fieldset = form.querySelector('.sam-pinquiry-form__fieldset');
      if (fieldset) fieldset.style.outline = 'none';
    }

    if (!allValid) return;

    /* GDPR check */
    var consent = form.querySelector('[name="gdpr_consent"]');
    if (consent && !consent.checked) {
      var wrapper = consent.closest('.sam-pinquiry-form__consent');
      if (wrapper) wrapper.style.outline = '2px solid #C4314B';
      return;
    }

    /* Loading state */
    var btn = form.querySelector('.sam-pinquiry-form__submit');
    var originalText = btn.textContent;
    btn.textContent = 'Sending...';
    btn.disabled = true;

    /* Collect data */
    var data = {};
    new FormData(form).forEach(function (val, key) {
      if (key === 'industries') {
        if (!data[key]) data[key] = [];
        data[key].push(val);
      } else {
        data[key] = val;
      }
    });

    /* GTM data layer push */
    if (typeof window.dataLayer !== 'undefined') {
      window.dataLayer.push({
        event: 'form_submission',
        form_type: 'partner_inquiry',
        source_page: window.location.pathname,
        company_type: data.company_type || '',
        industries: Array.isArray(data.industries) ? data.industries.join(',') : ''
      });
    }

    /* Simulate network delay, then show confirmation */
    setTimeout(function () {
      var firstName = data.first_name || '';
      if (confHeading && firstName) {
        confHeading.textContent = 'Thanks, ' + firstName + '. Our partnerships team will be in touch.';
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
