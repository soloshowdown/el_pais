
import os
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from logger import logger
from config import FULL_OPINION_URL


USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")

if not USERNAME or not ACCESS_KEY:
    raise Exception("BrowserStack credentials not set in environment variables")

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

capabilities_list = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11"
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "10"
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "os": "OS X",
        "osVersion": "Ventura"
    },
    {
        "deviceName": "iPhone 14",
        "realMobile": True,
        "osVersion": "16"
    },
    {
        "deviceName": "Samsung Galaxy S23",
        "realMobile": True,
        "osVersion": "13"
    }
]


def run_test(caps, index):
    logger.info(f"Starting BrowserStack session {index + 1}")

    options = Options()

    bstack_options = {
        "projectName": "El Pais Automation",
        "buildName": "Assignment v1",
        "sessionName": f"Opinion Test #{index + 1}"
    }

    options.set_capability("bstack:options", bstack_options)

    for key, value in caps.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    try:
        driver.get(FULL_OPINION_URL)
        time.sleep(5)
        logger.info(f"[Session {index + 1}] Page title: {driver.title}")
    finally:
        driver.quit()
        logger.info(f"Session {index + 1} completed")



threads = []

for i, caps in enumerate(capabilities_list):
    t = threading.Thread(target=run_test, args=(caps, i))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

logger.info("All BrowserStack sessions finished")