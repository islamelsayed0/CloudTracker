/**
 * theme.js - Theme Switching Functionality for Muzzy Tracker
 * 
 * This file handles the dark/light theme switching functionality.
 * It saves the user's preference to localStorage and applies the theme on page load.
 */

document.addEventListener('DOMContentLoaded', function() {
  // Check for saved theme preference or use default
  const currentTheme = localStorage.getItem('theme') || 'light';
  
  // Apply the theme on initial page load
  applyTheme(currentTheme);
  
  // Set the toggle switch to match the current theme
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.checked = currentTheme === 'dark';
    
    // Add event listener to the toggle switch
    themeToggle.addEventListener('change', function() {
      const theme = this.checked ? 'dark' : 'light';
      applyTheme(theme);
      localStorage.setItem('theme', theme);
    });
  }
});

/**
 * Apply the specified theme to the document
 * @param {string} theme - The theme to apply ('light' or 'dark')
 */
function applyTheme(theme) {
  const htmlRoot = document.getElementById('html-root');
  if (theme === 'dark') {
    htmlRoot.classList.add('dark-theme');
  } else {
    htmlRoot.classList.remove('dark-theme');
  }
}
