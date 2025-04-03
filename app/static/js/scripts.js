/**
 * scripts.js - Client-side functionality for Muzzy Tracker
 * 
 * This file handles:
 * - Smooth scrolling for navigation links
 * - Form validation for the login form
 * - Animation effects for page elements
 * 
 * The script uses vanilla JavaScript without dependencies
 * (except for Bootstrap's CSS classes for styling).
 */

/**
 * Initialize all functionality when the DOM is fully loaded
 * This ensures all elements are available for manipulation
 */
document.addEventListener('DOMContentLoaded', function() {
    /**
     * Smooth Scrolling Implementation
     * 
     * This adds smooth scrolling behavior to all anchor links on the page.
     * When a link with a hash (#) is clicked, the page smoothly scrolls
     * to the corresponding element instead of jumping instantly.
     */
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // Add click event listener to each anchor link
        anchor.addEventListener('click', function(e) {
            // Prevent default jump-to-anchor behavior
            e.preventDefault();
            
            // Get the target element's ID from the href attribute
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            // If target element exists, scroll to it
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 70, // Subtract navbar height for proper positioning
                    behavior: 'smooth' // Use smooth scrolling animation
                });
            }
        });
    });
    
    /**
     * Form Validation
     * 
     * Client-side validation for the login form to provide immediate feedback.
     * Validates:
     * - Email format (must contain @)
     * - Password length (minimum 6 characters)
     * 
     * Note: This is basic validation for UX purposes.
     * Server-side validation is still required for security.
     */
    const loginForm = document.querySelector('form');
    if (loginForm) {
        // Add submit event listener to the login form
        loginForm.addEventListener('submit', function(e) {
            // Get form input elements
            const emailInput = document.getElementById('email');
            const passwordInput = document.getElementById('password');
            
            let isValid = true;
            
            // Email validation - check for @ symbol
            // This is a simple check; a more comprehensive regex could be used
            if (!emailInput.value.includes('@')) {
                isValid = false;
                emailInput.classList.add('is-invalid'); // Add Bootstrap invalid class
            } else {
                emailInput.classList.remove('is-invalid');
            }
            
            // Password validation - check minimum length
            if (passwordInput.value.length < 6) {
                isValid = false;
                passwordInput.classList.add('is-invalid'); // Add Bootstrap invalid class
            } else {
                passwordInput.classList.remove('is-invalid');
            }
            
            // If validation fails, prevent form submission and show error message
            if (!isValid) {
                e.preventDefault(); // Stop form submission
                
                // Add error message if not already present
                // This prevents multiple error messages from stacking
                if (!document.querySelector('.validation-feedback')) {
                    const feedbackDiv = document.createElement('div');
                    feedbackDiv.className = 'alert alert-danger mt-3 validation-feedback';
                    feedbackDiv.textContent = 'Please check your email and password. Password must be at least 6 characters.';
                    loginForm.appendChild(feedbackDiv);
                }
            }
        });
    }
    
    /**
     * Scroll Animation
     * 
     * Adds animation classes to elements when they come into view during scrolling.
     * This creates a fade-in effect for feature cards and section titles.
     * 
     * Note: This implementation assumes the animate.css library is available.
     * If not present, these classes won't have any effect.
     */
    const animateOnScroll = function() {
        // Select elements to animate
        const elements = document.querySelectorAll('.feature-card, .section-title, .section-subtitle');
        
        elements.forEach(element => {
            // Get element's position relative to the viewport
            const elementPosition = element.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            // If element is in viewport (with 100px offset for earlier animation)
            if (elementPosition < windowHeight - 100) {
                // Add animation classes
                // These classes require animate.css to be included in the project
                element.classList.add('animate__animated', 'animate__fadeInUp');
            }
        });
    };
    
    // Set up scroll event listener and run initial check
    window.addEventListener('scroll', animateOnScroll); // Listen for scroll events
    animateOnScroll(); // Check elements on page load
});
