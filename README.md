# CloudSpend

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-green.svg)
![Flask](https://img.shields.io/badge/Flask-2.2.3-lightgrey.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![Azure](https://img.shields.io/badge/Azure-Ready-0078D4.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

<div align="center">
  <img src="app/static/images/cloudspend-logo.png" alt="CloudSpend Logo" width="300px" />
  <h3>Modern Financial Management in the Cloud</h3>
  <p><i>A portfolio project demonstrating full-stack development with Flask and Azure integration</i></p>
</div>

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Architecture](#-architecture)
- [Mobile Responsiveness](#-mobile-responsiveness)
- [Getting Started](#-getting-started)
- [Development](#-development)
- [Azure Deployment](#-azure-deployment)
- [Demo Mode](#-demo-mode)
- [Portfolio Context](#-portfolio-context)
- [Performance Optimizations](#-performance-optimizations)
- [Security Considerations](#-security-considerations)
- [License](#-license)

## 🔍 Overview

CloudSpend is a comprehensive financial management application designed to help users track expenses, manage budgets, and gain insights into their financial health. Built with a modern tech stack and deployed on Azure, this application showcases best practices in full-stack development.

**Important Note:** This is a portfolio demonstration project. While it includes integration points for real financial data, the application operates in demo mode with simulated data for showcase purposes.

## ✨ Features

### Core Functionality
- **Financial Dashboard**: Interactive overview of financial health with charts and summaries
- **Transaction Management**: Track, categorize, and analyze spending patterns
- **Budget Planning**: Create and monitor budgets with visual progress indicators
- **CSV Import**: Upload financial data from bank exports
- **Zakat Calculator**: Calculate Islamic almsgiving obligations based on assets

### Technical Highlights
- **Responsive Design**: Optimized for all devices from mobile to desktop
- **Dark Mode**: Toggle between light and dark themes with persistent preferences
- **Offline Support**: Core functionality works without an internet connection
- **Progressive Enhancement**: Basic features work in any browser, enhanced experience in modern browsers
- **Accessibility**: WCAG 2.1 AA compliant for inclusive user experience

## 🛠️ Technology Stack

### Frontend
- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Custom styling with CSS variables for theming
- **Bootstrap 5.3**: Latest version with enhanced mobile support
- **JavaScript**: Modern ES6+ features for interactive elements
- **Chart.js**: Responsive data visualization

### Backend
- **Python 3.9+**: Core programming language
- **Flask**: Lightweight web framework
- **Flask Extensions**:
  - Flask-WTF: Form handling and validation
  - Flask-Login: User session management
- **File-based Storage**: JSON data storage for demo purposes

### DevOps & Deployment
- **Azure App Service**: Cloud hosting platform
- **Azure Blob Storage**: Static asset storage
- **GitHub Actions**: CI/CD pipeline
- **Docker**: Containerization for consistent deployment

## 🏗️ Architecture

CloudSpend follows a modular MVC architecture designed for scalability and maintainability:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Browser   │────▶│  Flask App  │────▶│  File-based │
│   Client    │◀────│  (Server)   │◀────│   Storage   │
└─────────────┘     └─────────────┘     └─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │ Azure Blob  │
                    │  Storage    │
                    └─────────────┘
```

### Key Components:
- **Templates**: Jinja2 templates with inheritance for consistent UI
- **Static Assets**: CSS, JavaScript, and images served from Azure Blob Storage
- **Routes**: RESTful API endpoints for data operations
- **Services**: Business logic separated into service modules
- **Models**: Data structures and storage interfaces

## 📱 Mobile Responsiveness

CloudSpend is built with a mobile-first approach, ensuring optimal user experience across all devices:

- **Responsive Breakpoints**: Custom design for mobile, tablet, and desktop
- **Touch-Optimized**: Larger touch targets on mobile interfaces
- **Adaptive Layout**: Content reorganization based on screen size
- **Performance Optimized**: Minimized assets for faster mobile loading
- **Bottom Navigation**: Mobile-specific navigation pattern for thumb-friendly access

<div align="center">
  <img src="app/static/images/responsive-showcase.png" alt="Responsive Design Showcase" width="800px" />
</div>

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cloudspend.git
   cd cloudspend
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

5. **Run the application**
   ```bash
   flask run
   ```

6. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - You'll see the landing page with demo login

## 💻 Development

### Project Structure
```
cloudspend/
│
├── app/                      # Application code
│   ├── models/               # Data models
│   ├── services/             # Business logic services
│   ├── static/               # Static files (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/            # HTML templates
│       ├── accounts/         # Account-related templates
│       └── ...               # Other template categories
│
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

### Development Server
```bash
# Run with debug mode
flask --debug run
```

### Code Style
This project follows PEP 8 style guidelines for Python code. We recommend using:
- `flake8` for linting
- `black` for code formatting

## ☁️ Azure Deployment

CloudSpend is designed for deployment on Azure cloud services:

### Deployment Steps

1. **Create Azure Resources**
   ```bash
   # Install Azure CLI
   curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
   
   # Login to Azure
   az login
   
   # Create Resource Group
   az group create --name cloudspend-rg --location eastus
   
   # Create App Service Plan
   az appservice plan create --name cloudspend-plan --resource-group cloudspend-rg --sku B1
   
   # Create Web App
   az webapp create --name cloudspend --resource-group cloudspend-rg --plan cloudspend-plan --runtime "PYTHON|3.9"
   
   # Create Storage Account
   az storage account create --name cloudspendstore --resource-group cloudspend-rg --location eastus --sku Standard_LRS
   ```

2. **Configure GitHub Actions**
   - Create `.github/workflows/azure-deploy.yml` with deployment configuration
   - Add Azure credentials as GitHub secrets

3. **Deploy the Application**
   - Push to your deployment branch
   - GitHub Actions will automatically deploy to Azure

### Azure Architecture
<div align="center">
  <img src="app/static/images/azure-architecture.png" alt="Azure Architecture" width="600px" />
</div>

## 🎮 Demo Mode

CloudSpend operates in demo mode for portfolio demonstration purposes:

### Demo Features
- **Sample Data**: Pre-populated financial data for demonstration
- **Reset Functionality**: Reset to initial state with one click
- **No Real Data Processing**: Clear indicators that no actual financial data is processed
- **Simulated API Responses**: Mimics real API behavior without external dependencies

### Demo Limitations
- No actual database connection (uses file-based storage)
- No real financial institution connections
- Sample data is reset on application restart

## 🎨 Portfolio Context

This project was created as a portfolio demonstration of full-stack development skills:

### Showcased Skills
- **Frontend Development**: Modern, responsive UI with Bootstrap and custom CSS
- **Backend Development**: Flask application with proper architecture
- **Cloud Integration**: Azure deployment configuration
- **Security Practices**: Proper handling of sensitive data
- **Documentation**: Comprehensive code comments and project documentation
- **Mobile Optimization**: True responsive design for all devices

### Educational Purpose
This project is intended to demonstrate technical capabilities and is not meant for production use with real financial data.


## ⚡ Performance Optimizations

CloudSpend includes several performance optimizations:

- **Lazy Loading**: Images and non-critical resources load on demand
- **Code Splitting**: JavaScript is split into smaller chunks
- **Asset Minification**: CSS and JavaScript are minified for production
- **Caching Strategy**: Proper cache headers for static assets
- **Responsive Images**: Different image sizes for different devices
- **Critical CSS**: Inline critical styles for faster initial render

## 🔒 Security Considerations

While operating in demo mode, CloudSpend demonstrates security best practices:

- **HTTPS Only**: All communications use secure HTTPS
- **Content Security Policy**: Prevents XSS attacks
- **CSRF Protection**: All forms include CSRF tokens
- **Input Validation**: Server-side validation of all user inputs
- **Secure Headers**: Implementation of security-focused HTTP headers
- **No Sensitive Data**: Demo mode doesn't process real financial data

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**CloudSpend** - Developed for portfolio demonstration purposes
