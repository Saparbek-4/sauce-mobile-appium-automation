# 📱 Appium Mobile Automation Framework
**Automating Android UI Tests Using Appium + Pytest + BrowserStack + GitHub Actions**

Этот проект представляет собой полноценный mobile automation фреймворк, построенный с использованием современных подходов и инструментов:
Appium 2, Pytest, Page Object Model, Docker, GitHub Actions CI, Allure Reports, BrowserStack.

---

## 🚀 Features

- ✴ **Appium 2 + UiAutomator2**
- ✴ **Page Object Model (POM)**
- ✴ **Pytest markers**: smoke, functional, e2e, validation, security
- ✴ **Local Android emulator support**
- ✴ **BrowserStack cloud support**
- ✴ **Dockerized test execution**
- ✴ **GitHub Actions CI pipeline** running Smoke tests on PR
- ✴ **Allure Reports + GitHub Pages publishing**
- ✴ **Test results automatically posted to Pull Requests**

---

## 📂 Project Structure

```
project/
│── .github/workflows/
│     ├── pr-validation.yml       # Smoke tests in CI
│     └── regression.yml          # (optional) Full regression (disabled)
│
│── apk/
│     └── Android.SauceLabs.Mobile.Sample.app.apk
│
│── config/
│     ├── dev.yml                 # Local Appium capabilities
│     └── browserstack.yml        # BrowserStack capabilities
│
│── drivers/
│     ├── android_driver.py
│     ├── browserstack_driver.py
│     └── driver_factory.py
│
│── locators/
│── pages/
│── tests/
│── utils/
│
│── docker-compose.yml
│── Dockerfile
│── run_tests.sh
│── requirements.txt
│── pytest.ini
│── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Saparbek-4/sauce-mobile-appium-automation.git
cd sauce-mobile-appium-automation
```

---

## 📦 Local Test Execution

**Requirements:**
- Python 3.10+
- Appium 2 installed
- Android emulator or real device

**Run local tests:**

```bash
pytest --env=local --alluredir=allure-results
```

**Generate Allure report:**

```bash
allure serve allure-results
```

---

## ☁️ Running Tests on BrowserStack

**Set environment variables:**

```bash
export BS_USERNAME="your_username"
export BS_ACCESS_KEY="your_key"
export BS_APP_ID="bs://your-uploaded-app-id"
```

**Run in cloud:**

```bash
pytest --env=browserstack --alluredir=allure-results
```

---

## 🐳 Running in Docker

**Build container:**

```bash
docker build -t mobile-tests .
```

**Run smoke tests:**

```bash
docker run \
  -e BS_USERNAME=$BS_USERNAME \
  -e BS_ACCESS_KEY=$BS_ACCESS_KEY \
  -e BS_APP_ID=$BS_APP_ID \
  mobile-tests pytest -m smoke --env=browserstack --alluredir=allure-results
```

---

## 🔄 Continuous Integration (CI)

✔ **Smoke Tests** run automatically for every Pull Request

**Workflow:** `.github/workflows/pr-validation.yml`

**What it does:**
- Builds Docker container
- Runs smoke tests on BrowserStack
- Generates Allure Report
- Uploads results as GitHub artifact
- Deploys Allure to GitHub Pages
- Comments PR with test results

### 🔗 Live Allure Report (GitHub Pages)

👉 **https://saparbek-4.github.io/sauce-mobile-appium-automation/**

---

## 🧪 Test Types Covered

| Type       | Description                          |
|------------|--------------------------------------|
| **Smoke**      | Fast, critical-path validation (CI)  |
| **Functional** | Core feature verification            |
| **E2E**        | Full purchase flow                   |
| **Validation** | Input checks & error messages        |
| **Security**   | Access restrictions & logout behavior|
| **UI**         | Scrolling, visual states             |

---

## 📘 Framework Architecture

✔ **Page Object Model**

Each screen has:
- Locators
- Methods
- Validations

**Example:**

```python
class LoginPage(BasePage):
    def login(self, username, password):
        self.type(LoginLocators.USERNAME, username)
        self.type(LoginLocators.PASSWORD, password)
        self.tap(LoginLocators.LOGIN_BUTTON)
```

---

## 🧰 Technologies Used

| Tool            | Purpose                      |
|-----------------|------------------------------|
| **Appium 2**        | Mobile automation            |
| **Pytest**          | Test runner                  |
| **UiAutomator2**    | Android automation driver    |
| **BrowserStack**    | Cloud device farm            |
| **Docker**          | Isolated test execution      |
| **GitHub Actions**  | Continuous Integration       |
| **Allure Report**   | Beautiful test reporting     |

---

## 📝 Author

**Saparbek Kozhanazar**  
*Automation QA Engineer*  
📧 saparbek@example.com *(укажи реальную почту)*

---

## 🟢 This project demonstrates:

✔ Умение строить mobile automation framework с нуля  
✔ CI/CD интеграцию для автотестов  
✔ Кросс-платформенное исполнение (local + cloud)  
✔ Работа с Docker  
✔ Работа с Appium 2 и BrowserStack  
✔ Full POM + test design подход