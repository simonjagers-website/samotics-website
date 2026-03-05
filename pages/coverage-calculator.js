/* ============================================================
   SAMOTICS COVERAGE CALCULATOR PAGE — JavaScript
   Paste into Bricks Code Element → JavaScript tab
   ============================================================ */

(function () {
  'use strict';

  /* ── Skip-link target ── */
  var main = document.getElementById('main-content');
  if (main && !main.getAttribute('tabindex')) {
    main.setAttribute('tabindex', '-1');
  }

  /* ── DOM refs ── */
  var calcForm       = document.getElementById('calcForm');
  var calcResults    = document.getElementById('calcResults');
  var recalcBtn      = document.getElementById('recalcBtn');
  var captureForm    = document.getElementById('captureForm');
  var captureSection = document.getElementById('calcCapture');
  var captureConf    = document.getElementById('captureConfirmation');

  var inputTotal     = document.getElementById('calc-total');
  var inputMonitored = document.getElementById('calc-monitored');
  var inputCost      = document.getElementById('calc-cost');
  var inputFailures  = document.getElementById('calc-failures');
  var inputCurrency  = document.getElementById('calc-currency');

  var resultGap           = document.getElementById('resultGap');
  var resultGapDetail     = document.getElementById('resultGapDetail');
  var resultRisk          = document.getElementById('resultRisk');
  var resultRiskDetail    = document.getElementById('resultRiskDetail');
  var resultBenchmark     = document.getElementById('resultBenchmark');
  var resultBenchmarkDetail = document.getElementById('resultBenchmarkDetail');
  var resultRecommendation  = document.getElementById('resultRecommendation');

  /* ── Stored calc values for lead capture ── */
  var lastCalc = {};

  /* ============================================================
     CALCULATOR LOGIC
     ============================================================ */

  function validateCalcForm() {
    var valid = true;
    var inputs = [inputTotal, inputMonitored, inputCost, inputFailures];

    inputs.forEach(function (el) {
      el.classList.remove('has-error');
      if (!el.value || parseFloat(el.value) < 0) {
        el.classList.add('has-error');
        valid = false;
      }
    });

    /* Total must be > 0 */
    if (inputTotal.value && parseInt(inputTotal.value, 10) < 1) {
      inputTotal.classList.add('has-error');
      valid = false;
    }

    /* Monitored cannot exceed total */
    if (inputMonitored.value && inputTotal.value) {
      if (parseInt(inputMonitored.value, 10) > parseInt(inputTotal.value, 10)) {
        inputMonitored.classList.add('has-error');
        valid = false;
      }
    }

    return valid;
  }

  function formatNumber(n, currency) {
    if (currency) {
      return currency + n.toLocaleString('en', { maximumFractionDigits: 0 });
    }
    return n.toLocaleString('en', { maximumFractionDigits: 0 });
  }

  function calculate() {
    var total     = parseInt(inputTotal.value, 10);
    var monitored = parseInt(inputMonitored.value, 10);
    var cost      = parseFloat(inputCost.value);
    var failures  = parseFloat(inputFailures.value);
    var currency  = inputCurrency.value;

    var unmonitored = total - monitored;
    var gapPct      = Math.round((unmonitored / total) * 100);
    var coveragePct = 100 - gapPct;
    var annualRisk  = Math.round(unmonitored * cost * (failures / Math.max(unmonitored, 1)));

    /* Benchmark tier */
    var tier, tierLabel, tierClass, recommendation;
    if (coveragePct < 40) {
      tier = 'critical';
      tierLabel = 'Critical gap';
      tierClass = 'tier-critical';
      recommendation = '<strong>Critical coverage gap.</strong> With ' + gapPct + '% of your fleet unmonitored, you have significant blind spots. Undetected failures on ' + formatNumber(unmonitored) + ' assets represent ' + formatNumber(annualRisk, currency) + ' in estimated annual risk. An asset audit can identify which assets to prioritise first — start with your highest-risk, highest-cost equipment.';
    } else if (coveragePct < 65) {
      tier = 'moderate';
      tierLabel = 'Moderate gap';
      tierClass = 'tier-moderate';
      recommendation = '<strong>Moderate coverage gap.</strong> You\'re monitoring ' + coveragePct + '% of your fleet, which is near the industry average. But ' + formatNumber(unmonitored) + ' unmonitored assets still represent ' + formatNumber(annualRisk, currency) + ' in annual risk. Closing this gap doesn\'t require a massive investment — ESA technology installs at the MCC in under 30 minutes per asset.';
    } else {
      tier = 'low';
      tierLabel = 'Low gap';
      tierClass = 'tier-low';
      recommendation = '<strong>Low coverage gap.</strong> At ' + coveragePct + '% coverage you\'re ahead of most operations. The remaining ' + formatNumber(unmonitored) + ' unmonitored assets may include hard-to-reach or low-priority equipment. SAM4\'s MCC-based installation can close the gap on assets that were previously impractical to monitor.';
    }

    /* Store for lead capture */
    lastCalc = {
      total: total,
      monitored: monitored,
      unmonitored: unmonitored,
      gapPct: gapPct,
      annualRisk: annualRisk,
      currency: currency,
      tier: tier
    };

    /* Populate results */
    resultGap.textContent       = gapPct + '%';
    resultGapDetail.textContent = formatNumber(unmonitored) + ' of ' + formatNumber(total) + ' assets unmonitored';
    resultRisk.textContent      = formatNumber(annualRisk, currency);
    resultRiskDetail.textContent = 'Estimated annual exposure from unmonitored failures';
    resultBenchmark.textContent = tierLabel;
    resultBenchmarkDetail.textContent = 'Industry average: 60–70% coverage';

    resultRecommendation.innerHTML = recommendation;
    resultRecommendation.className = 'sam-calc-results__recommendation ' + tierClass;

    /* Show results */
    calcResults.hidden = false;
    calcResults.scrollIntoView({ behavior: 'smooth', block: 'start' });

    /* GTM */
    if (window.dataLayer) {
      window.dataLayer.push({
        event: 'coverage_calculator_completed',
        gap_percentage: gapPct,
        risk_tier: tier
      });
    }
  }

  calcForm.addEventListener('submit', function (e) {
    e.preventDefault();
    if (validateCalcForm()) {
      calculate();
    }
  });

  /* ── Recalculate ── */
  recalcBtn.addEventListener('click', function () {
    calcResults.hidden = true;
    calcForm.querySelector('.sam-calc-form__submit').scrollIntoView({ behavior: 'smooth', block: 'center' });
  });


  /* ============================================================
     LEAD CAPTURE FORM
     ============================================================ */

  var FREE_DOMAINS = ['gmail.com','yahoo.com','hotmail.com','outlook.com','aol.com','icloud.com','mail.com','protonmail.com','live.com','msn.com'];

  function validateCaptureForm() {
    var valid = true;
    var fname   = document.getElementById('capture-fname');
    var email   = document.getElementById('capture-email');
    var company = document.getElementById('capture-company');
    var gdpr    = document.getElementById('capture-gdpr');

    [fname, email, company].forEach(function (el) {
      el.classList.remove('has-error');
      if (!el.value.trim()) {
        el.classList.add('has-error');
        valid = false;
      }
    });

    /* Email format */
    if (email.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
      email.classList.add('has-error');
      valid = false;
    }

    /* GDPR */
    if (!gdpr.checked) {
      valid = false;
    }

    return valid;
  }

  captureForm.addEventListener('submit', function (e) {
    e.preventDefault();

    /* Honeypot */
    if (document.getElementById('capture-website').value) return;

    if (!validateCaptureForm()) return;

    var fname = document.getElementById('capture-fname').value.trim();
    var email = document.getElementById('capture-email').value.trim();

    /* Free email warning (non-blocking) */
    var domain = email.split('@')[1];
    if (domain && FREE_DOMAINS.indexOf(domain.toLowerCase()) !== -1) {
      /* Just log, don't block */
    }

    var submitBtn = captureForm.querySelector('.sam-calc-capture__submit');
    submitBtn.textContent = 'Sending…';
    submitBtn.disabled = true;

    /* Simulate submission delay */
    setTimeout(function () {
      /* GTM */
      if (window.dataLayer) {
        window.dataLayer.push({
          event: 'coverage_calculator_lead',
          form_type: 'coverage_calculator',
          gap_percentage: lastCalc.gapPct || null,
          risk_tier: lastCalc.tier || null
        });
      }

      /* Show confirmation */
      captureForm.hidden = true;
      captureConf.hidden = false;
      document.getElementById('captureConfMsg').textContent = 'Thanks, ' + fname + '. We\u2019ll prepare your personalised coverage assessment.';
      captureConf.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 800);
  });

  /* ── Inline blur validation for capture form ── */
  ['capture-fname', 'capture-email', 'capture-company'].forEach(function (id) {
    var el = document.getElementById(id);
    if (el) {
      el.addEventListener('blur', function () {
        if (!el.value.trim()) {
          el.classList.add('has-error');
        } else {
          el.classList.remove('has-error');
        }
      });
    }
  });

})();
