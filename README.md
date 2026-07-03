# SauceDemo Test Automation Suite

Automated UI test suite for saucedemo.com built with Python, Selenium, and pytest,
following the Page Object Model design pattern.

## What it covers
- Login: valid credentials, invalid credentials, locked-out user, empty-field validation (parametrized)
- Shopping flow: add-to-cart badge updates, cart page navigation

## Tech stack
Python · Selenium · pytest · webdriver-manager · GitHub Actions CI

## Project structure
    pages/       - Page Object Model classes (one per page)
    tests/       - Test files + shared fixtures (conftest.py)

## Running locally
    python -m venv venv
    source venv/bin/activate   # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    pytest -v --html=report.html --self-contained-html

## CI
Tests run automatically on every push via GitHub Actions (see `.github/workflows/tests.yml`).
