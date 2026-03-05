/*
  ROI Calculator JavaScript
  Paste this into the Bricks Code element JS tab
  Handles calculations, animations, and form interactions
*/

document.addEventListener('DOMContentLoaded', function() {
  // Form elements
  const assetsInput = document.getElementById('assets-input');
  const downtimeCostInput = document.getElementById('downtime-cost-input');
  const downtimeHoursInput = document.getElementById('downtime-hours-input');
  const maintenanceSpendInput = document.getElementById('maintenance-spend-input');
  const industrySelect = document.getElementById('industry-select');
  const calculateBtn = document.getElementById('calculate-btn');
  const resultsPanel = document.getElementById('results-panel');

  // Result elements
  const savingsValue = document.getElementById('savings-value');
  const sam4CostValue = document.getElementById('sam4-cost-value');
  const roiValue = document.getElementById('roi-value');
  const paybackValue = document.getElementById('payback-value');
  const currentBar = document.getElementById('current-bar');
  const withSamBar = document.getElementById('with-sam-bar');

  // Gate form
  const gateForm = document.getElementById('gate-form');

  // Format currency with EUR symbol and thousands separator
  function formatCurrency(value) {
    return '€' + value.toLocaleString('de-DE', {
      minimumFractionDigits: 0,
      maximumFractionDigits: 0,
    });
  }

  // Validate form inputs
  function validateInputs() {
    const assets = parseInt(assetsInput.value) || 0;
    const downtimeCost = parseInt(downtimeCostInput.value) || 0;
    const downtimeHours = parseInt(downtimeHoursInput.value) || 0;
    const maintenanceSpend = parseInt(maintenanceSpendInput.value) || 0;

    if (assets <= 0 || downtimeCost <= 0) {
      alert('Please enter valid values for assets and downtime cost.');
      return false;
    }

    return true;
  }

  // Calculate ROI
  function calculateROI() {
    if (!validateInputs()) return;

    const assets = parseInt(assetsInput.value) || 100;
    const downtimeCost = parseInt(downtimeCostInput.value) || 5000;
    const downtimeHours = parseInt(downtimeHoursInput.value) || 200;
    const maintenanceSpend = parseInt(maintenanceSpendInput.value) || 500000;

    // Calculations
    const downtimeSavings = downtimeCost * downtimeHours * 0.35;
    const maintenanceSavings = maintenanceSpend * 0.15;
    const totalSavings = downtimeSavings + maintenanceSavings;

    const sam4Cost = assets * 500;
    const netBenefit = totalSavings - sam4Cost;
    const roi = (netBenefit / sam4Cost) * 100;
    const payback = (sam4Cost / totalSavings) * 12;

    // Current total costs
    const currentCosts = downtimeCost * downtimeHours + maintenanceSpend;
    const costsWithSAM = currentCosts - totalSavings + sam4Cost;

    // Animate results panel
    resultsPanel.classList.add('active');

    // Animate numbers
    animateValue(savingsValue, totalSavings, 'currency');
    animateValue(sam4CostValue, sam4Cost, 'currency');
    animateValue(roiValue, roi, 'percent');
    animateValue(paybackValue, payback, 'months');

    // Animate chart bars
    const currentBarPercent = 100;
    const samBarPercent = (costsWithSAM / currentCosts) * 100;

    animateBarWidth(currentBar, currentBarPercent);
    animateBarWidth(withSamBar, samBarPercent);
  }

  // Animate number counting
  function animateValue(element, targetValue, format) {
    const startValue = 0;
    const duration = 1000;
    const startTime = Date.now();

    function update() {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const currentValue = Math.floor(startValue + (targetValue - startValue) * progress);

      if (format === 'currency') {
        element.textContent = formatCurrency(currentValue);
      } else if (format === 'percent') {
        element.textContent = currentValue + '%';
      } else if (format === 'months') {
        element.textContent = Math.round(currentValue * 10) / 10 + ' mo';
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    update();
  }

  // Animate bar width
  function animateBarWidth(element, targetPercent) {
    const startPercent = 0;
    const duration = 800;
    const startTime = Date.now();

    function update() {
      const elapsed = Date.now() - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const currentPercent = startPercent + (targetPercent - startPercent) * progress;

      element.style.width = currentPercent + '%';

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    update();
  }

  // Event listeners
  calculateBtn.addEventListener('click', calculateROI);

  // Allow Enter key in inputs to trigger calculation
  [assetsInput, downtimeCostInput, downtimeHoursInput, maintenanceSpendInput].forEach(input => {
    input.addEventListener('keypress', function(e) {
      if (e.key === 'Enter') {
        calculateROI();
      }
    });
  });

  // Gate form submission
  gateForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const name = document.getElementById('gate-name').value.trim();
    const email = document.getElementById('gate-email').value.trim();
    const company = document.getElementById('gate-company').value.trim();

    if (!name || !email || !company) {
      alert('Please fill in all fields.');
      return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      alert('Please enter a valid email address.');
      return;
    }

    // Placeholder: Log form data (replace with actual submission logic)
    console.log({
      name: name,
      email: email,
      company: company,
      assets: assetsInput.value,
      downtimeCost: downtimeCostInput.value,
      downtimeHours: downtimeHoursInput.value,
      maintenanceSpend: maintenanceSpendInput.value,
      industry: industrySelect.value,
    });

    // Show success message
    alert('Thank you! Your ROI report will be sent to ' + email);

    // Clear form
    gateForm.reset();
  });

  // Prevent invalid input (negative numbers)
  [assetsInput, downtimeCostInput, downtimeHoursInput, maintenanceSpendInput].forEach(input => {
    input.addEventListener('input', function() {
      if (this.value < 0) {
        this.value = 0;
      }
    });
  });
});
