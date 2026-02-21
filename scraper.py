import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

logger = logging.getLogger(__name__)

def handle_cookies(driver):
    try:
        wait = WebDriverWait(driver, 5)
        accept_button = wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(text(),'Accept') or contains(text(),'Agree') or contains(text(),'Aceptar')]"
            ))
        )
        accept_button.click()
        logger.info("Cookie consent accepted")
        time.sleep(2)
    except TimeoutException:
        logger.info("No cookie banner found")

def scrape_article(driver, url):
    driver.get(url)
    handle_cookies(driver)

    wait = WebDriverWait(driver, 10)

    try:
        title = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        ).text
    except:
        title = "N/A"

    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    content = " ".join([p.text for p in paragraphs if len(p.text) > 30])

    return title, content