import pytest
import os
import datetime
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Global driver instance
driver = None

# Generate a timestamped folder for reports
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_dir = os.path.join(os.path.dirname(__file__), "Reports",f"Report_(timestamp)" )

if not os.path.exists(report_dir):
    os.makedirs(report_dir)


def pytest_addoption(parser):
    """Add command-line options for browser selection and headless mode."""
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome/firefox/edge")
    parser.addoption("--headless", action="store", default="false", help="Run tests in headless mode: true/false")


@pytest.fixture(scope="class")
def setupbrowser(request):
    """Fixture to initialize and close the browser."""
    global driver
    browser_name = request.config.getoption("browser_name").lower()
    headless_mode = request.config.getoption("headless").lower() == "true"

    if browser_name == "chrome":
        chrome_options = Options()
        if headless_mode:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = FirefoxOptions()
        if headless_mode:
            firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)

    elif browser_name == "edge":
        driver = webdriver.Edge()

    else:
        raise ValueError("Invalid browser name. Use chrome, firefox, or edge.")

    driver.get("https://infotimeqa.azurewebsites.net/")
    driver.maximize_window()
    driver.implicitly_wait(40)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Capture screenshot on test failure and attach it to the report.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ('call', 'setup'):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = f"{report.nodeid.replace('::', '_')}.png"
            screenshot_path = os.path.join(report_dir, file_name)
            _capture_screenshot(screenshot_path)
            if file_name:
                html = (
                    f'<div><img src="{screenshot_path}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(path):
    """Capture and save a screenshot."""
    driver.get_screenshot_as_file(path)


def pytest_html_report_title(report):
    """Set custom report title."""
    report.title = "Automation Test Report"


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Customize PyTest HTML report summary (Fixed Issue)."""
    prefix.extend(["Custom PyTest Execution Summary"])


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Set up report file paths."""
    html_report = os.path.join(report_dir, "pytest_report.html")
    config.option.htmlpath = html_report  # PyTest HTML Report

def pytest_configure(config):
    """Set up Allure report directory."""
    allure_dir = os.path.join(report_dir, "allure-results")
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)
    config.option.allure_report_dir = allure_dir