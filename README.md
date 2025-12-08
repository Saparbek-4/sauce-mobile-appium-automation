# Appium Demo Project (Android)
Demo Appium + Pytest framework for SauceLabs Demo App (Android).

## Features
- Page Object Model
- Pytest fixtures (driver factory)
- Allure reporting ready
- Sample tests (login, add to cart)
- CI pipeline template (GitHub Actions)

## Quick start (local)
1. Install dependencies: `pip install -r requirements.txt`
2. Start Android emulator or connect device with USB debugging.
3. Install APK: `adb install -r apk/Android-MyDemoApp-release.apk`
4. Run tests: `pytest -q --alluredir=reports/allure-results`
5. Generate Allure report: `allure serve reports/allure-results`

## Project structure
See folder layout in repository root.
