


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
import os
import pytest_html

@pytest.fixture(scope="class")
def init_driver(request):

    supported_browsers = {
        "chrome", "ch", "firefox", "ff"
    }

    browser = os.environ.get('BROWSER', None)

    if not browser:
        raise Exception("Environment varialbe 'BROWSER' must be set.")

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Browser not supported. Supported browsers are: {supported_browsers}")

    if browser in ("chrome", "ch"):
        driver = webdriver.Chrome()
    elif browser in ("firefox", "ff"):
        driver = webdriver.Firefox()

    request.cls.driver = driver
    yield
    driver.quit()

# pytest-html
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if "init_driver" in item.fixturenames else False

            if is_frontend_test:
                results_dir = os.environ.get('RESULTS_DIR')
                if not results_dir: 
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")

                screenshot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                driver_fixture.cls.driver.save_screenshot(screenshot_path)
                extras.append(pytest_html.extras.image(screenshot_path))
        report.extras = extras