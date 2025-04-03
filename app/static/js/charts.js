/**
 * charts.js - Chart configurations for Muzzy Tracker
 * 
 * This file contains all the chart configurations and initialization functions
 * for the Muzzy Tracker dashboard. It uses Chart.js to create interactive
 * visualizations of financial data.
 */

// Initialize all charts when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Initialize charts with sample data (in a real app, this would come from the backend)
  initNetWorthChart();
  initSpendingTrendsChart();
  initInvestmentPortfolioChart();
  initCategorySpendingChart();
});

/**
 * Initialize the Net Worth Timeline Chart
 * Shows the progression of net worth, assets, and liabilities over time
 */
function initNetWorthChart() {
  // Sample data - in a real app, this would come from an API call
  const data = {
    labels: ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr'],
    netWorth: [38000, 39500, 41000, 42500, 43800, 44500, 45250],
    assets: [55000, 57000, 59000, 61000, 63000, 64500, 65800],
    liabilities: [17000, 17500, 18000, 18500, 19200, 20000, 20550]
  };
  
  const ctx = document.getElementById('netWorthChart');
  if (!ctx) return; // Exit if element doesn't exist
  
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: data.labels,
      datasets: [
        {
          label: 'Net Worth',
          data: data.netWorth,
          borderColor: '#0B6E4F',
          backgroundColor: 'rgba(11, 110, 79, 0.1)',
          fill: true,
          tension: 0.4
        },
        {
          label: 'Assets',
          data: data.assets,
          borderColor: '#28a745',
          borderDash: [5, 5],
          fill: false,
          tension: 0.4
        },
        {
          label: 'Liabilities',
          data: data.liabilities,
          borderColor: '#dc3545',
          borderDash: [5, 5],
          fill: false,
          tension: 0.4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          mode: 'index',
          intersect: false,
          callbacks: {
            label: function(context) {
              return context.dataset.label + ': $' + context.raw.toLocaleString();
            }
          }
        },
        legend: {
          position: 'top',
        }
      },
      scales: {
        y: {
          beginAtZero: false,
          ticks: {
            callback: function(value) {
              return '$' + value.toLocaleString();
            }
          }
        }
      }
    }
  });
}

/**
 * Initialize the Spending Trends Chart
 * Shows spending patterns over time by category
 */
function initSpendingTrendsChart() {
  // Sample data - in a real app, this would come from an API call
  const data = {
    labels: ['Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr'],
    datasets: [
      {
        label: 'Housing',
        data: [1850, 1850, 1850, 1850, 1850, 1850, 1850],
        backgroundColor: '#4E79A7'
      },
      {
        label: 'Food',
        data: [650, 720, 850, 580, 620, 710, 680],
        backgroundColor: '#F28E2B'
      },
      {
        label: 'Transportation',
        data: [320, 350, 380, 290, 310, 340, 330],
        backgroundColor: '#E15759'
      },
      {
        label: 'Entertainment',
        data: [250, 320, 420, 180, 210, 240, 260],
        backgroundColor: '#76B7B2'
      },
      {
        label: 'Other',
        data: [430, 480, 520, 390, 410, 450, 470],
        backgroundColor: '#59A14F'
      }
    ]
  };
  
  const ctx = document.getElementById('spendingTrendsChart');
  if (!ctx) return; // Exit if element doesn't exist
  
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: data.labels,
      datasets: data.datasets
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          mode: 'index',
          intersect: false,
          callbacks: {
            label: function(context) {
              return context.dataset.label + ': $' + context.raw.toLocaleString();
            }
          }
        },
        legend: {
          position: 'top',
        }
      },
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true,
          ticks: {
            callback: function(value) {
              return '$' + value;
            }
          }
        }
      }
    }
  });
}

/**
 * Initialize the Investment Portfolio Chart
 * Shows the allocation of investments by type
 */
function initInvestmentPortfolioChart() {
  // Sample data - in a real app, this would come from an API call
  const data = {
    labels: ['Stocks', 'Bonds', 'ETFs', 'Real Estate', 'Crypto', 'Cash'],
    datasets: [{
      data: [45, 15, 20, 10, 5, 5],
      backgroundColor: [
        '#4E79A7', 
        '#F28E2B', 
        '#E15759', 
        '#76B7B2', 
        '#59A14F',
        '#EDC948'
      ],
      borderWidth: 1
    }]
  };
  
  const ctx = document.getElementById('investmentPortfolioChart');
  if (!ctx) return; // Exit if element doesn't exist
  
  new Chart(ctx, {
    type: 'doughnut',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          callbacks: {
            label: function(context) {
              const label = context.label || '';
              const value = context.raw || 0;
              const total = context.dataset.data.reduce((a, b) => a + b, 0);
              const percentage = Math.round((value / total) * 100);
              return `${label}: ${percentage}% ($${Math.round(percentage * 328 / 100).toLocaleString()})`;
            }
          }
        },
        legend: {
          position: 'right',
        }
      },
      cutout: '70%'
    }
  });
}

/**
 * Initialize the Category Spending Chart
 * Shows spending breakdown by category for the current month
 */
function initCategorySpendingChart() {
  // Sample data - in a real app, this would come from an API call
  const data = {
    labels: ['Housing', 'Food', 'Transportation', 'Entertainment', 'Utilities', 'Shopping', 'Other'],
    datasets: [{
      data: [1850, 680, 330, 260, 220, 310, 160],
      backgroundColor: [
        '#4E79A7', 
        '#F28E2B', 
        '#E15759', 
        '#76B7B2', 
        '#59A14F',
        '#EDC948',
        '#B07AA1'
      ],
      borderWidth: 1
    }]
  };
  
  const ctx = document.getElementById('categorySpendingChart');
  if (!ctx) return; // Exit if element doesn't exist
  
  new Chart(ctx, {
    type: 'pie',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          callbacks: {
            label: function(context) {
              const label = context.label || '';
              const value = context.raw || 0;
              const total = context.dataset.data.reduce((a, b) => a + b, 0);
              const percentage = Math.round((value / total) * 100);
              return `${label}: $${value.toLocaleString()} (${percentage}%)`;
            }
          }
        },
        legend: {
          position: 'right',
        }
      }
    }
  });
}

/**
 * Initialize the Debt Payoff Projection Chart
 * Shows projected debt reduction over time with different payment strategies
 */
function initDebtPayoffChart() {
  // Sample data - in a real app, this would come from an API call
  const data = {
    labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
    datasets: [
      {
        label: 'Minimum Payments',
        data: [20550, 20100, 19650, 19200, 18750, 18300, 17850, 17400, 16950, 16500],
        borderColor: '#dc3545',
        backgroundColor: 'rgba(220, 53, 69, 0.1)',
        fill: true,
        tension: 0.4
      },
      {
        label: 'Recommended Plan',
        data: [20550, 19500, 18450, 17400, 16350, 15300, 14250, 13200, 12150, 11100],
        borderColor: '#fd7e14',
        backgroundColor: 'rgba(253, 126, 20, 0.1)',
        fill: true,
        tension: 0.4
      },
      {
        label: 'Aggressive Plan',
        data: [20550, 18950, 17350, 15750, 14150, 12550, 10950, 9350, 7750, 6150],
        borderColor: '#28a745',
        backgroundColor: 'rgba(40, 167, 69, 0.1)',
        fill: true,
        tension: 0.4
      }
    ]
  };
  
  const ctx = document.getElementById('debtPayoffChart');
  if (!ctx) return; // Exit if element doesn't exist
  
  new Chart(ctx, {
    type: 'line',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          mode: 'index',
          intersect: false,
          callbacks: {
            label: function(context) {
              return context.dataset.label + ': $' + context.raw.toLocaleString();
            }
          }
        },
        legend: {
          position: 'top',
        }
      },
      scales: {
        y: {
          reverse: true,
          ticks: {
            callback: function(value) {
              return '$' + value.toLocaleString();
            }
          }
        }
      }
    }
  });
}

/**
 * Initialize the Income Sources Chart
 * Shows breakdown of income by source
 */
function initIncomeSourcesChart() {
  // Sample data - in a real app, this would come from an API call
  const data = {
    labels: ['Jan', 'Feb', 'Mar', 'Apr'],
    datasets: [
      {
        label: 'Primary Job',
        data: [3250, 3250, 3250, 3250],
        backgroundColor: '#4E79A7'
      },
      {
        label: 'Side Hustle',
        data: [850, 920, 780, 850],
        backgroundColor: '#F28E2B'
      },
      {
        label: 'Investments',
        data: [320, 350, 380, 420],
        backgroundColor: '#59A14F'
      },
      {
        label: 'Other',
        data: [150, 120, 180, 200],
        backgroundColor: '#B07AA1'
      }
    ]
  };
  
  const ctx = document.getElementById('incomeSourcesChart');
  if (!ctx) return; // Exit if element doesn't exist
  
  new Chart(ctx, {
    type: 'bar',
    data: data,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        tooltip: {
          mode: 'index',
          intersect: false,
          callbacks: {
            label: function(context) {
              return context.dataset.label + ': $' + context.raw.toLocaleString();
            }
          }
        },
        legend: {
          position: 'top',
        }
      },
      scales: {
        x: {
          stacked: true,
        },
        y: {
          stacked: true,
          ticks: {
            callback: function(value) {
              return '$' + value;
            }
          }
        }
      }
    }
  });
}
