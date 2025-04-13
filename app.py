"""
app.py - Main Flask Application for Muzzy Tracker

This file serves as the entry point for the Muzzy Tracker finance web application.
It initializes the Flask application, defines routes, and handles HTTP requests.
The application allows users to track finances, analyze spending patterns, and calculate Zakat.

Routes:
    / - Landing page with hero section, about section, and login form
    /login - Handles login form submission (POST)
    /register - Placeholder for user registration

Future integrations:
    - Plaid API for bank account connections
    - Azure Database for MySQL for data storage
    - Azure Blob Storage for file uploads
"""

# Import necessary Flask modules
from flask import Flask, render_template, request, redirect, url_for, flash

# Initialize and configure Flask application
app = Flask(__name__, 
            static_folder='app/static',  # Location of static assets (CSS, JS, images)
            template_folder='app/templates')  # Location of HTML templates
            
# Secret key for session management and CSRF protection
# SECURITY: Change this to a random secret key in production
app.secret_key = 'your_secret_key'

# Route definitions
@app.route('/')
def index():
    """
    Render the landing page (login.html).
    
    This page includes:
    - Hero section with headline and feature icons
    - About section with feature descriptions
    - Login form
    
    Returns:
        Rendered HTML template for the landing page
    """
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    """
    Handle login form submission.
    
    This is currently a placeholder for actual authentication logic.
    In a production environment, this would:
    1. Validate user credentials against a database
    2. Create a user session
    3. Redirect to the appropriate dashboard
    
    Parameters (from form):
        email: User's email address
        password: User's password
        remember: Whether to remember the user's session
    
    Returns:
        Redirect to dashboard page after successful login
    """
    # Extract form data
    email = request.form.get('email')
    password = request.form.get('password')
    remember = 'remember' in request.form
    
    # TODO: Implement actual authentication logic
    # - Validate email format and password requirements
    # - Check credentials against database
    # - Create user session
    
    # For demonstration purposes, we'll redirect to the dashboard
    # In a real application, this would only happen after successful authentication
    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle user registration.
    
    GET: Renders the registration form
    POST: Processes the form submission, validates data, and creates a new user account
    
    Form fields:
    - first_name: User's first name
    - last_name: User's last name
    - email: User's email address (used for login)
    - phone: User's phone number
    - password: User's password
    - confirm_password: Password confirmation
    - terms: Agreement to terms and conditions
    
    Returns:
        GET: Rendered registration form template
        POST: Redirect to dashboard on success or back to form with errors
    """
    # If the request is POST, process the form submission
    if request.method == 'POST':
        # Extract form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        terms_accepted = 'terms' in request.form
        
        # Validate form data
        errors = []
        
        # Check if all required fields are provided
        if not all([first_name, last_name, email, phone, password, confirm_password]):
            errors.append('All fields are required')
        
        # Validate email format (basic check)
        if email and '@' not in email:
            errors.append('Invalid email format')
        
        # Check if passwords match
        if password != confirm_password:
            errors.append('Passwords do not match')
        
        # Check password strength (basic check)
        if password and len(password) < 8:
            errors.append('Password must be at least 8 characters long')
        
        # Check terms acceptance
        if not terms_accepted:
            errors.append('You must accept the terms and conditions')
        
        # If there are validation errors, flash them and return to the form
        if errors:
            for error in errors:
                flash(error, 'danger')
            return render_template('register.html')
        
        # TODO: Check if email already exists in the database
        # TODO: Hash the password before storing
        # TODO: Store user data in the database
        
        # For now, just log the data (would be replaced with database operations)
        app.logger.info(f"New user registration: {first_name} {last_name}, {email}, {phone}")
        
        # Flash success message
        flash('Account created successfully! You can now log in.', 'success')
        
        # Redirect to login page
        return redirect(url_for('index') + '#login')
    
    # If the request is GET, render the registration form
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    """
    Render the main dashboard page.
    
    This page includes:
    - Financial overview with net worth, assets, and liabilities
    - Spending trends visualization
    - Investment portfolio tracking
    - Credit card debt management
    - Monthly subscriptions
    - Recent transactions
    - Upcoming bills and payments
    
    Returns:
        Rendered HTML template for the dashboard
    """
    # TODO: Implement authentication check
    # - Verify user is logged in
    # - Redirect to login page if not authenticated
    
    # TODO: Fetch user's financial data
    # - Connect to database or Plaid API
    # - Retrieve account balances, transactions, etc.
    
    return render_template('dashboard.html')

@app.route('/disclaimer')
def disclaimer():
    """
    Render the disclaimer page.
    
    This page includes:
    - Comprehensive disclaimer about the application not providing financial advice
    - Limitation of liability statements
    - Use at your own risk notices
    
    Returns:
        Rendered HTML template for the disclaimer
    """
    return render_template('disclaimer.html')

@app.route('/terms')
def terms():
    """
    Render the terms of use page.
    
    This page includes:
    - User agreement terms
    - Intellectual property rights
    - User responsibilities
    - Prohibited activities
    - Limitation of liability
    - Other standard terms of use content
    
    Returns:
        Rendered HTML template for the terms of use
    """
    return render_template('terms.html')

@app.route('/privacy')
def privacy():
    """
    Render the privacy policy page.
    
    This page includes:
    - Information collection practices
    - How information is used and shared
    - Data security measures
    - User rights regarding their data
    - Third-party services information
    - Other standard privacy policy content
    
    Returns:
        Rendered HTML template for the privacy policy
    """
    return render_template('privacy.html')

@app.route('/import')
def import_csv():
    """
    Render the CSV import page.
    
    This page includes:
    - File upload interface
    - Column mapping functionality
    - Data preview and validation
    - Import confirmation
    
    The CSV import feature provides an alternative to Plaid integration
    for users who prefer not to connect their bank accounts directly.
    
    Returns:
        Rendered HTML template for the CSV import page
    """
    # TODO: Implement authentication check
    # - Verify user is logged in
    # - Redirect to login page if not authenticated
    
    return render_template('import.html')

@app.route('/import/upload', methods=['POST'])
def upload_csv_file():
    """
    Handle CSV file upload.
    
    This endpoint:
    1. Validates the uploaded file
    2. Saves it to a temporary location
    3. Reads the CSV data
    4. Suggests column mappings
    
    Returns:
        JSON response with file ID, column names, and suggested mappings
    """
    from app.services.csv_service import CSVService
    import json
    
    # Initialize CSV service
    csv_service = CSVService()
    
    # Check if file was uploaded
    if 'file' not in request.files:
        return json.dumps({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    # Check if filename is empty
    if file.filename == '':
        return json.dumps({'error': 'No file selected'}), 400
    
    # Check file extension
    if not file.filename.endswith('.csv'):
        return json.dumps({'error': 'File must be a CSV'}), 400
    
    try:
        # Save the file to a temporary location
        file_path = csv_service.save_uploaded_file(file)
        
        # Read the CSV file
        df = csv_service.read_csv(file_path)
        
        # Get column names
        columns = df.columns.tolist()
        
        # Suggest column mappings
        suggested_mapping = csv_service.suggest_column_mapping(df)
        
        # Get sample data for preview (first 5 rows)
        sample_data = df.head(5).to_dict('records')
        
        # Return the file path, columns, and suggested mappings
        return json.dumps({
            'file_path': file_path,
            'columns': columns,
            'suggested_mapping': suggested_mapping,
            'sample_data': sample_data
        }), 200
    
    except Exception as e:
        return json.dumps({'error': str(e)}), 500

@app.route('/import/map', methods=['POST'])
def map_csv_columns():
    """
    Process column mapping for CSV import.
    
    This endpoint:
    1. Applies the user-selected column mappings
    2. Converts dates to a standard format
    3. Normalizes amounts
    4. Categorizes transactions
    
    Returns:
        JSON response with preview data
    """
    from app.services.csv_service import CSVService
    import json
    
    # Initialize CSV service
    csv_service = CSVService()
    
    # Get request data
    data = request.get_json()
    
    if not data:
        return json.dumps({'error': 'No data provided'}), 400
    
    file_path = data.get('file_path')
    mapping = data.get('mapping')
    date_format = data.get('date_format')
    amount_format = data.get('amount_format', 'negative_expense')
    
    if not file_path or not mapping:
        return json.dumps({'error': 'Missing required parameters'}), 400
    
    try:
        # Read the CSV file
        df = csv_service.read_csv(file_path)
        
        # Apply column mapping
        df = csv_service.apply_column_mapping(df, mapping)
        
        # Convert dates if date column and format are provided
        if 'date' in df.columns and date_format:
            df = csv_service.convert_dates(df, 'date', date_format)
        
        # Normalize amounts
        df = csv_service.normalize_amounts(df, amount_format)
        
        # Categorize transactions
        df = csv_service.categorize_transactions(df)
        
        # Validate the data
        issues = csv_service.validate_data(df)
        
        # Generate preview
        preview = csv_service.generate_preview(df, issues)
        
        # Return the preview data
        return json.dumps({
            'file_path': file_path,
            'preview': preview
        }), 200
    
    except Exception as e:
        return json.dumps({'error': str(e)}), 500

@app.route('/import/preview', methods=['POST'])
def preview_csv_import():
    """
    Generate a detailed preview of the CSV import.
    
    This endpoint:
    1. Applies any user adjustments to the data
    2. Performs final validation
    3. Generates statistics and potential issues
    
    Returns:
        JSON response with detailed preview data
    """
    from app.services.csv_service import CSVService
    import json
    
    # Initialize CSV service
    csv_service = CSVService()
    
    # Get request data
    data = request.get_json()
    
    if not data:
        return json.dumps({'error': 'No data provided'}), 400
    
    file_path = data.get('file_path')
    skip_duplicates = data.get('skip_duplicates', True)
    auto_categorize = data.get('auto_categorize', True)
    fix_issues = data.get('fix_issues', True)
    
    if not file_path:
        return json.dumps({'error': 'Missing file path'}), 400
    
    try:
        # Read the CSV file with previously applied mappings
        # (This would be stored in a session in a real application)
        df = csv_service.read_csv(file_path)
        
        # Apply any additional processing based on user options
        if auto_categorize:
            df = csv_service.categorize_transactions(df)
        
        # Validate the data
        issues = csv_service.validate_data(df)
        
        # Generate detailed preview
        preview = csv_service.generate_preview(df, issues)
        
        # Return the preview data
        return json.dumps({
            'file_path': file_path,
            'preview': preview
        }), 200
    
    except Exception as e:
        return json.dumps({'error': str(e)}), 500

@app.route('/import/process', methods=['POST'])
def process_csv_import():
    """
    Process the final CSV import.
    
    This endpoint:
    1. Processes the CSV data with all user-confirmed settings
    2. Stores the transactions in the system
    3. Generates an import summary
    
    Returns:
        JSON response with import summary
    """
    from app.services.csv_service import CSVService
    from app.models.transaction import Transaction, TransactionBatch, add_transaction_batch
    from datetime import datetime
    import json
    
    # Initialize CSV service
    csv_service = CSVService()
    
    # Get request data
    data = request.get_json()
    
    if not data:
        return json.dumps({'error': 'No data provided'}), 400
    
    file_path = data.get('file_path')
    
    if not file_path:
        return json.dumps({'error': 'Missing file path'}), 400
    
    try:
        # Read the CSV file with previously applied mappings
        df = csv_service.read_csv(file_path)
        
        # Process the import
        import_result = csv_service.process_import(df)
        
        # Create Transaction objects
        transactions = []
        for t_data in import_result['transactions']:
            transaction = Transaction.from_dict(t_data)
            transactions.append(transaction)
        
        # Create a TransactionBatch
        batch = TransactionBatch(
            batch_id=import_result['summary']['batch_id'],
            transactions=transactions,
            import_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        
        # Add the batch to the database
        add_transaction_batch(batch)
        
        # Clean up the temporary file
        csv_service.cleanup_temp_file(file_path)
        
        # Return the import summary
        return json.dumps({
            'success': True,
            'summary': batch.to_dict()
        }), 200
    
    except Exception as e:
        return json.dumps({'error': str(e)}), 500

@app.route('/accounts/bank')
def bank_accounts():
    """
    Render the bank accounts page.
    
    This page includes:
    - List of all bank accounts with current balances
    - Account details and transaction history
    - Account management options (add, edit, remove)
    - Balance trends visualization
    
    Returns:
        Rendered HTML template for the bank accounts page
    """
    # TODO: Implement authentication check
    # TODO: Fetch bank account data from database or Plaid API
    
    return render_template('accounts/bank.html')

@app.route('/accounts/credit')
def credit_cards():
    """
    Render the credit cards page.
    
    This page includes:
    - List of all credit cards with current balances and limits
    - Credit utilization visualization
    - Payment information and due dates
    - Interest calculations and payoff projections
    
    Returns:
        Rendered HTML template for the credit cards page
    """
    # TODO: Implement authentication check
    # TODO: Fetch credit card data from database or Plaid API
    
    return render_template('accounts/credit.html')

@app.route('/accounts/investments')
def investment_accounts():
    """
    Render the investment accounts page.
    
    This page includes:
    - Portfolio overview with current values
    - Asset allocation breakdown
    - Performance metrics and comparison to benchmarks
    - Individual holdings and their performance
    
    Returns:
        Rendered HTML template for the investment accounts page
    """
    # TODO: Implement authentication check
    # TODO: Fetch investment account data from database or Plaid API
    
    return render_template('accounts/investments.html')

@app.route('/transactions')
def transactions():
    """
    Render the transactions page.
    
    This page includes:
    - Monthly view of all transactions
    - Filtering and search functionality
    - Category management
    - Transaction details and export options
    
    Returns:
        Rendered HTML template for the transactions page
    """
    # TODO: Implement authentication check
    # TODO: Fetch transaction data from database or Plaid API
    
    return render_template('transactions.html')

@app.route('/subscriptions')
def subscriptions():
    """
    Render the subscriptions page.
    
    This page includes:
    - List of all recurring monthly payments
    - Payment schedule and renewal alerts
    - Subscription management options
    - Cost analysis and optimization suggestions
    
    Returns:
        Rendered HTML template for the subscriptions page
    """
    # TODO: Implement authentication check
    # TODO: Fetch subscription data from database
    
    return render_template('subscriptions.html')

@app.route('/budget')
def budget():
    """
    Render the budget page.
    
    This page includes:
    - Manual income setup with tax calculator
    - Category-based budget allocation
    - Budget vs. actual comparison
    - Budget insights and recommendations
    
    Returns:
        Rendered HTML template for the budget page
    """
    # TODO: Implement authentication check
    # TODO: Fetch budget data from database
    
    return render_template('budget.html')

@app.route('/zakat')
def zakat():
    """
    Render the Zakat calculator page.
    
    This page includes:
    - Zakat calculation form with different asset types
    - Explanation of Zakat eligibility criteria
    - Calculation of 2.5% on eligible wealth
    - Recommendations for Zakat distribution
    
    Returns:
        Rendered HTML template for the Zakat calculator
    """
    # TODO: Implement authentication check
    
    return render_template('zakat.html')

@app.route('/settings')
def settings():
    """
    Render the settings page.
    
    This page includes:
    - Dark mode toggle
    - Sign out button
    - Profile settings
    - Notification preferences
    - Currency display options
    
    Returns:
        Rendered HTML template for the settings page
    """
    # TODO: Implement authentication check
    
    return render_template('settings.html')

@app.route('/notifications')
def notifications():
    """
    Render the notifications page.
    
    This page includes:
    - List of all notifications
    - Notification filtering options
    - Mark as read functionality
    - Notification preferences link
    
    Returns:
        Rendered HTML template for the notifications page
    """
    # TODO: Implement authentication check
    # TODO: Fetch notifications from database
    
    return render_template('notifications.html')

@app.route('/privacy-security')
def privacy_security():
    """
    Render the privacy and security settings page.
    
    This page includes:
    - Two-factor authentication settings
    - Privacy controls
    - Data management options
    - Security logs
    - Connected devices
    
    Returns:
        Rendered HTML template for the privacy and security page
    """
    # TODO: Implement authentication check
    # TODO: Fetch security logs and connected devices
    
    return render_template('privacy_security.html')

@app.route('/logout')
def logout():
    """
    Handle user logout.
    
    This route:
    1. Clears the user's session
    2. Redirects to the login page
    3. Displays a success message
    
    Returns:
        Redirect to login page
    """
    # TODO: Implement actual session clearing
    # session.clear()
    
    flash('You have been successfully logged out.', 'success')
    return redirect(url_for('index'))

# Application entry point
if __name__ == '__main__':
    """
    Run the Flask application when this file is executed directly.
    
    The debug=True setting enables:
    - Auto-reload on code changes
    - Detailed error pages
    - Debug console for exceptions
    
    SECURITY: Set debug=False in production environments
    """
    app.run(debug=True)  # Development server with debug mode
