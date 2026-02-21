from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# 🔐 Use environment variables (BEST PRACTICE)
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

drivers = []

for caps in capabilities_list:
    options = Options()

    # 🔹 BrowserStack specific options
    bstack_options = {
        "projectName": "El Pais Automation",
        "buildName": "Assignment v1",
        "sessionName": "Opinion Section Test"
    }

    options.set_capability("bstack:options", bstack_options)

    # 🔹 Set browser / device capabilities
    for key, value in caps.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    drivers.append(driver)

# Run tests
for driver in drivers:
    driver.get("https://elpais.com/opinion/")
    time.sleep(5)
    print(driver.title)
    driver.quit()