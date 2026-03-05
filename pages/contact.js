/* ============================================================
   SAMOTICS CONTACT PAGE — JavaScript
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
  var intentBtns      = document.querySelectorAll('.sam-contact-intent__btn');
  var forms           = document.querySelectorAll('.sam-contact-form');
  var expectationEl   = document.getElementById('contact-expectation');

  /* ── Intent → form mapping ── */
  var intentConfig = {
    demo: {
      formId: 'form-demo',
      expectation: 'We\'ll schedule a technical demo within 5 business days. You\'ll speak with a specialist, not a salesperson.'
    },
    audit: {
      formId: 'form-audit',
      expectation: 'We\'ll prepare your asset audit scope and reach out within 2 business days.'
    },
    executive: {
      formId: 'form-executive',
      expectation: 'A member of our leadership team will reach out within 1 business day.'
    },
    security: {
      formId: null, // redirects to /platform/security
      expectation: null
    },
    partner: {
      formId: 'form-partner',
      expectation: 'Our partnerships team will be in touch within 2 business days.'
    }
  };

  var activeIntent = null;

  /* ── Read intent from URL ── */
  function getIntentFromURL() {
    var params = new URLSearchParams(window.location.search);
    return params.get('intent');
  }

  /* ── Show form for intent ── */
  function selectIntent(intent) {
    if (!intentConfig[intent]) return;

    // Security intent → redirect
    if (intent === 'security') {
      window.location.href = '/platform/security#security-docs';
      return;
    }

    activeIntent = intent;

    // Update button states
    intentBtns.forEach(function (btn) {
      var isActive = btn.getAttribute('data-intent') === intent;
      btn.classList.toggle('sam-contact-intent__btn--active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    });

    // Hide all forms, show the matching one
    forms.forEach(function (form) {
      form.hidden = true;
    });
    var targetForm = document.getElementById(intentConfig[intent].formId);
    if (targetForm) {
      targetForm.hidden = false;
    }

    // Show expectation line
    if (expectationEl && intentConfig[intent].expectation) {
      expectationEl.textContent = intentConfig[intent].expectation;
      expectationEl.hidden = false;
    } else if (expectationEl) {
      expectationEl.hidden = true;
    }

    // Scroll form into view
    if (targetForm) {
      targetForm.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  /* ── Intent button clicks ── */
  intentBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      selectIntent(this.getAttribute('data-intent'));
    });
  });

  /* ── Free email warning ── */
  var freeProviders = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'live.com', 'aol.com', 'icloud.com'];

  function checkFreeEmail(input) {
    var hintEl = input.parentElement.querySelector('.sam-contact-form__hint');
    if (!hintEl) return;

    var val = input.value.trim();
    var domain = val.indexOf('@') !== -1 ? val.split('@')[1].toLowerCase() : '';

    if (domain && freeProviders.indexOf(domain) !== -1) {
      hintEl.hidden = false;
    } else {
      hintEl.hidden = true;
    }
  }

  document.querySelectorAll('input[type="email"]').forEach(function (input) {
    input.addEventListener('blur', function () {
      checkFreeEmail(this);
    });
  });

  /* ── Inline validation on blur ── */
  function validateField(field) {
    var input = field.querySelector('input, select, textarea');
    if (!input) return true;

    var isRequired = input.hasAttribute('required');
    var isEmpty = !input.value.trim();

    // Remove previous error
    field.classList.remove('sam-contact-form__field--error');
    var existingError = field.querySelector('.sam-contact-form__field-error');
    if (existingError) existingError.remove();

    // Check required
    if (isRequired && isEmpty) {
      showFieldError(field, getErrorMessage(input, 'required'));
      return false;
    }

    // Check email format
    if (input.type === 'email' && !isEmpty) {
      var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailPattern.test(input.value.trim())) {
        showFieldError(field, 'Please enter a valid email address');
        return false;
      }
    }

    return true;
  }

  function showFieldError(field, message) {
    field.classList.add('sam-contact-form__field--error');
    var errorEl = document.createElement('span');
    errorEl.className = 'sam-contact-form__field-error';
    errorEl.textContent = message;
    errorEl.style.display = 'block';
    field.appendChild(errorEl);
  }

  function getErrorMessage(input, type) {
    var label = input.parentElement.querySelector('label');
    var name = label ? label.textContent.replace(' *', '') : 'This field';

    if (type === 'required') {
      return 'Please enter your ' + name.toLowerCase();
    }
    return 'Please check ' + name.toLowerCase();
  }

  // Attach blur validation to all form fields
  document.querySelectorAll('.sam-contact-form__field').forEach(function (field) {
    var input = field.querySelector('input, select, textarea');
    if (input) {
      input.addEventListener('blur', function () {
        validateField(field);
      });
      // Clear error on input
      input.addEventListener('input', function () {
        field.classList.remove('sam-contact-form__field--error');
        var err = field.querySelector('.sam-contact-form__field-error');
        if (err) err.remove();
      });
    }
  });

  /* ── Form submission ── */
  forms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Check honeypot
      var hp = form.querySelector('.sam-contact-form__hp input');
      if (hp && hp.value) return; // bot detected

      // Validate all fields
      var fields = form.querySelectorAll('.sam-contact-form__field');
      var isValid = true;
      fields.forEach(function (field) {
        if (!validateField(field)) {
          isValid = false;
        }
      });

      // Check GDPR consent
      var consent = form.querySelector('input[name="gdpr_consent"]');
      if (consent && !consent.checked) {
        isValid = false;
        var consentWrapper = consent.closest('.sam-contact-form__consent');
        if (consentWrapper) {
          consentWrapper.style.outline = '2px solid #C4314B';
          consentWrapper.style.outlineOffset = '4px';
          setTimeout(function () {
            consentWrapper.style.outline = '';
            consentWrapper.style.outlineOffset = '';
          }, 3000);
        }
      }

      if (!isValid) {
        // Focus first error
        var firstError = form.querySelector('.sam-contact-form__field--error input, .sam-contact-form__field--error select, .sam-contact-form__field--error textarea');
        if (firstError) firstError.focus();
        return;
      }

      // Submit — show loading state
      var submitBtn = form.querySelector('.sam-contact-form__submit');
      var originalText = submitBtn.textContent;
      submitBtn.textContent = 'Sending...';
      submitBtn.disabled = true;

      // Placeholder: replace with actual form handler (HubSpot, etc.)
      // For now, simulate success after a short delay
      setTimeout(function () {
        // Get first name for confirmation
        var fnameInput = form.querySelector('input[name="first_name"]');
        var fname = fnameInput ? fnameInput.value : '';

        // Replace form with confirmation
        var confirmationMessages = {
          'form-demo': 'Thanks, ' + fname + '. We\'ll be in touch within 1 business day to schedule your demo.',
          'form-audit': 'Thanks, ' + fname + '. We\'ll prepare your asset audit scope and reach out within 2 business days.',
          'form-executive': 'Thanks, ' + fname + '. A member of our leadership team will reach out within 1 business day.',
          'form-partner': 'Thanks, ' + fname + '. Our partnerships team will be in touch within 2 business days.'
        };

        form.innerHTML = '<div class="sam-contact-form__confirmation">' +
          '<p class="sam-contact-form__confirmation-text">' + (confirmationMessages[form.id] || 'Thanks! We\'ll be in touch soon.') + '</p>' +
          '</div>';

        // Fire GTM event (placeholder)
        if (typeof window.dataLayer !== 'undefined') {
          var eventMap = {
            'form-demo': 'demo_request',
            'form-audit': 'asset_audit_request',
            'form-executive': 'executive_inquiry',
            'form-partner': 'partner_inquiry'
          };
          window.dataLayer.push({
            event: 'form_submission',
            form_type: eventMap[form.id] || 'contact',
            source_page: window.location.pathname,
            intent: activeIntent
          });
        }
      }, 800);
    });
  });

  /* ── Auto-select intent from URL parameter ── */
  var urlIntent = getIntentFromURL();
  if (urlIntent && intentConfig[urlIntent]) {
    selectIntent(urlIntent);
  }

})();
