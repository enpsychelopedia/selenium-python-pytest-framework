# Selenium Python Pytest Framework

## Overview

A UI test automation framework built with Python, Selenium WebDriver, and Pytest. The framework uses the Page Object Model (POM) to organize page interactions and locators, with reusable helper methods for common Selenium operations.

This project was built to practice and demonstrate maintainable test automation, test organization, reusable components, and automated test reporting.

## Tech Stack

- **Python** – Programming language
- **Selenium WebDriver** – Browser automation
- **Pytest** – Test framework and test execution
- **Page Object Model (POM)** – Test structure and maintainability
- **pytest-html** – HTML test reporting
- **Git & GitHub** – Version control and project hosting

## Project Structure

```text
seleframework/
├── assets/                         # Static project assets
├── configs/                        # Framework configuration
├── helpers/                        # Reusable framework utilities
├── src/
│   ├── pages/                      # Page Object classes
│   │   └── locators/               # Page-specific locators
│   └── tests/                      # Automated test cases
├── conftest.py                     # Pytest fixtures and hooks
├── pytest.ini                      # Pytest configuration and custom markers
├── .gitignore                      # Files excluded from version control
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation

```

## Test Coverage

The framework currently covers the following UI test scenarios:

- **New User Registration** – Verifies that a new user can successfully create an account.
- **Invalid User Login** – Verifies that invalid login credentials are handled correctly.
- **Guest User End-to-End Checkout** – Verifies the complete shopping flow from product selection through checkout and order confirmation.

## Features

- Page Object Model (POM) architecture for organized and maintainable test code
- Reusable Selenium helper methods for common browser interactions
- Pytest fixtures for browser setup and teardown
- Custom Pytest markers for test case organization
- **Randomized test data generation** for user registration
- Explicit waits to improve test stability
- Automated HTML test reporting with pytest-html
- Screenshot capture for failed tests

## Test Reporting

The framework uses `pytest-html` to generate HTML test reports. Screenshots are automatically captured when a test fails and attached to the HTML report for easier debugging.

Generated test reports and screenshots are stored in the `results/` directory and are excluded from version control through `.gitignore`.

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/enpsychelopedia/selenium-python-pytest-framework.git
cd selenium-python-pytest-framework
```

### 2. Create a virtual environment 

```bash
python -m venv venv_seleniumframework
```

### 3. Activate the virtual environment 

```bash
**Windows (Command Prompt):**
venv_seleniumframework\Scripts\activate.bat
```

### 4. Install dependencies 

```bash
pip install -r requirements.txt
```

### 5. Run the tests

```bash
pytest 
```

## Running Specific Tests

Run all tests:

```bash
pytest
```

Run a specific test case using its Pytest marker:

```bash
pytest -m tcid1
```

```bash
pytest -m tcid2
```

```bash
pytest -m tcid3
```

To generate an HTML test report:

```bash
pytest --html=results/result.html
```

The generated report will be saved as `result.html` inside the `results/` directory.