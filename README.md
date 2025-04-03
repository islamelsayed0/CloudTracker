# Muzzy Tracker

![Version](https://img.shields.io/badge/version-0.1.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-green.svg)
![Flask](https://img.shields.io/badge/Flask-2.2.3-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

Muzzy Tracker is a comprehensive full-stack finance web application designed to help users track their finances, analyze spending patterns, and calculate Zakat (Islamic almsgiving). The application securely connects to users' bank accounts and investment platforms to provide a complete financial overview.

## 📋 Table of Contents

- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Configuration](#-configuration)
- [Development](#-development)
- [Deployment](#-deployment)
- [Security Considerations](#-security-considerations)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Bank Account Integration**: Connect securely to your bank accounts using Plaid API
- **Investment Tracking**: Connect to investment platforms like Robinhood
- **Smart Analytics**: Visualize your spending patterns with interactive charts
- **Zakat Calculator**: Calculate your annual Zakat obligation with precision
- **Secure & Private**: Your financial data is encrypted and secure
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Semantic markup for structure
- **CSS3**: Custom styling with responsive design
- **Bootstrap 5**: UI framework for responsive components
- **JavaScript**: Client-side validation and interactivity

### Backend
- **Python 3.9+**: Core programming language
- **Flask**: Web framework
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and validation
- **Azure Database for MySQL**: Primary data storage
- **Azure Blob Storage**: File storage for uploads

### APIs & Integrations
- **Plaid API**: Secure bank account integration
- **Azure App Service**: Hosting platform

## 📁 Project Structure

```
muzzy_tracker/
│
├── app/                      # Application code
│   ├── static/               # Static files (CSS, JS, images)
│   │   ├── css/
│   │   │   └── styles.css    # Custom styles
│   │   └── js/
│   │       └── scripts.js    # Client-side functionality
│   ├── templates/            # HTML templates
│   │   ├── base.html         # Base template with common structure
│   │   ├── login.html        # Landing page with login form
│   │   └── ...               # Other templates
│   └── ...                   # Python modules
│
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+**: The application requires Python 3.9 or newer
- **pip**: Python package manager
- **Git**: Version control system (for cloning the repository)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/muzzy_tracker.git
   cd muzzy_tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file and add your credentials

6. **Run the application**
   ```bash
   flask run
   ```

7. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - You should see the landing page with the login form

## ⚙️ Configuration

The application uses environment variables for configuration. These are stored in a `.env` file in the root directory.

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `FLASK_APP` | Main Flask application file | `app.py` |
| `FLASK_ENV` | Environment (development, production) | `development` |
| `SECRET_KEY` | Secret key for session management | `your_random_secret_key` |
| `PLAID_CLIENT_ID` | Plaid API client ID | `your_plaid_client_id` |
| `PLAID_SECRET` | Plaid API secret | `your_plaid_secret` |
| `PLAID_ENV` | Plaid environment (sandbox, development, production) | `sandbox` |
| `AZURE_STORAGE_CONNECTION_STRING` | Azure Blob Storage connection string | `your_connection_string` |
| `AZURE_MYSQL_SERVER` | Azure MySQL server hostname | `your_server.database.windows.net` |
| `AZURE_MYSQL_DATABASE` | MySQL database name | `your_database_name` |
| `AZURE_MYSQL_USERNAME` | MySQL username | `your_username` |
| `AZURE_MYSQL_PASSWORD` | MySQL password | `your_password` |

### Obtaining API Credentials

#### Plaid API
1. Sign up for a [Plaid account](https://dashboard.plaid.com/signup)
2. Create a new project
3. Navigate to the API keys section
4. Copy your client ID and secrets for the desired environment

#### Azure Services
1. Create an [Azure account](https://azure.microsoft.com/free/)
2. Set up Azure Database for MySQL
3. Create an Azure Blob Storage account
4. Copy the connection strings and credentials from the Azure Portal

## 💻 Development

### Running in Development Mode

```bash
# Set Flask to development mode
export FLASK_ENV=development  # Unix/macOS
set FLASK_ENV=development     # Windows

# Run with debug mode
flask run --debug
```

### Code Style

This project follows PEP 8 style guidelines for Python code. We recommend using tools like:
- `flake8` for linting
- `black` for code formatting

### Testing

```bash
# Run tests (when implemented)
pytest
```

## 🚢 Deployment

The application is designed to be deployed on Azure cloud services:

### Azure Deployment Steps

1. **Prepare the application**
   - Ensure `FLASK_ENV=production` in your `.env` file
   - Generate a strong `SECRET_KEY`
   - Set up proper logging

2. **Create Azure resources**
   - Azure App Service for hosting the application
   - Azure Database for MySQL for data storage
   - Azure Blob Storage for file storage

3. **Configure deployment**
   - Set up GitHub Actions or Azure DevOps for CI/CD
   - Configure environment variables in Azure App Service
   - Set up database migrations

4. **Deploy the application**
   - Push to your deployment branch
   - Monitor the deployment process
   - Verify the application is running correctly

### Deployment Architecture

```
[Users] → [Azure App Service] → [Azure Database for MySQL]
                             ↘ [Azure Blob Storage]
```

## 🔒 Security Considerations

- **Environment Variables**: Never commit `.env` files to version control
- **API Keys**: Keep Plaid API keys and Azure credentials secure
- **HTTPS**: Always use HTTPS in production
- **Authentication**: Implement proper user authentication
- **Data Encryption**: Encrypt sensitive data at rest and in transit
- **Input Validation**: Validate all user inputs on both client and server
- **Regular Updates**: Keep dependencies updated to patch security vulnerabilities

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Muzzy Tracker** - Developed with ❤️ for better financial management
