# 🧪 Mini Dashboard Automation Suite

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/ry727777/mini-dashboard-automation/ci.yml?branch=main)
![Allure Report](https://img.shields.io/badge/Allure-Report-orange)
![Python](https://img.shields.io/badge/python-3.11-blue)

This project is an end-to-end automation testing suite for the **Mini Dashboard Web Application**, built with **Selenium**, **Pytest**, and **Page Object Model (POM)** design. It integrates **GitHub Actions** for CI/CD and generates test reports using **Allure**.

> Designed to run seamlessly in both local and CI environments (e.g., GitHub Actions).

---

## 🚀 Features

- ✅ Selenium-based UI test automation
- ✅ Pytest test execution with custom markers (e.g., `@regression`)
- ✅ Allure HTML test reports
- ✅ GitHub Actions workflow for automatic test execution on PRs and pushes
- ✅ Clean Page Object Model (POM) design
- ✅ Easy scalability and maintainability

---

## 📂 Project Structure

mini-dashboard-automation/
├── tests/ # Test cases
│ └── test_add_user_data.py
├── Action/ # Page Object Model classes
│ └── AddUserOrder.py
├── conftest.py # Pytest fixtures (e.g., WebDriver setup)
├── requirements.txt # Python dependencies
├── .github/workflows/ci.yml # GitHub Actions workflow
└── README.md # Project documentation


--- yaml

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.11+
- Google Chrome (latest)
- ChromeDriver (auto-handled by `webdriver_manager`)

### 📥 Installation

```bash
# Clone the repository
git clone https://github.com/ry727777/mini-dashboard-automation.git
cd mini-dashboard-automation

# (Optional but recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install all dependencies
pip install -r requirements.txt


- Run Regression suits
    pytest -m regression --alluredir=allure-results

- Generate report
    allure generate allure-results --clean -o allure-report
    allure open allure-report


- Author
    Rahul Yadav (https://www.linkedin.com/in/ry727777/)
    
