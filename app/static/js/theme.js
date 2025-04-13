/**
 * theme.js - Theme Switching Functionality for CloudSpend
 * 
 * This file handles the dark/light theme switching functionality.
 * It saves the user's preference to localStorage and applies the theme on page load.
 * The theme toggle is available in both desktop and mobile versions.
 */

document.addEventListener('DOMContentLoaded', function() {
  // Check for saved theme preference, system preference, or use default
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const currentTheme = savedTheme || (prefersDark ? 'dark' : 'light');
  
  // Apply the theme on initial page load
  applyTheme(currentTheme);
  
  // Update the toggle button icons to match the current theme
  updateToggleIcons(currentTheme);
  
  // Set up event listeners for both desktop and mobile toggle buttons
  const desktopToggle = document.getElementById('theme-toggle-desktop');
  const mobileToggle = document.getElementById('theme-toggle-mobile');
  
  if (desktopToggle) {
    desktopToggle.addEventListener('click', toggleTheme);
  }
  
  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleTheme);
  }
  
  // Listen for system theme changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    if (!localStorage.getItem('theme')) {
      // Only auto-switch if user hasn't manually set a preference
      const newTheme = e.matches ? 'dark' : 'light';
      applyTheme(newTheme);
      updateToggleIcons(newTheme);
    }
  });
});

/**
 * Toggle between light and dark themes
 */
function toggleTheme() {
  const htmlRoot = document.getElementById('html-root');
  const isDark = htmlRoot.classList.contains('dark-theme');
  const newTheme = isDark ? 'light' : 'dark';
  
  applyTheme(newTheme);
  updateToggleIcons(newTheme);
  localStorage.setItem('theme', newTheme);
}

/**
 * Apply the specified theme to the document
 * @param {string} theme - The theme to apply ('light' or 'dark')
 */
function applyTheme(theme) {
  const htmlRoot = document.getElementById('html-root');
  if (theme === 'dark') {
    htmlRoot.classList.add('dark-theme');
    document.querySelector('meta[name="theme-color"]').setAttribute('content', '#121212');
  } else {
    htmlRoot.classList.remove('dark-theme');
    document.querySelector('meta[name="theme-color"]').setAttribute('content', '#3498db');
  }
}

/**
 * Update the toggle button icons based on the current theme
 * @param {string} theme - The current theme ('light' or 'dark')
 */
function updateToggleIcons(theme) {
  const desktopToggle = document.getElementById('theme-toggle-desktop');
  const mobileToggle = document.getElementById('theme-toggle-mobile');
  
  if (desktopToggle) {
    const desktopIcon = desktopToggle.querySelector('i');
    if (desktopIcon) {
      desktopIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
    }
  }
  
  if (mobileToggle) {
    const mobileIcon = mobileToggle.querySelector('i');
    if (mobileIcon) {
      mobileIcon.className = theme === 'dark' ? 'bi bi-sun-fill' : 'bi bi-moon-fill';
    }
  }
}
