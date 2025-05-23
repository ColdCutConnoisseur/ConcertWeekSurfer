"""This will house TM functionality"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils import price_cleanup


def run_ticketmaster_min_price_check(driver: webdriver, url_to_visit: str) -> float:
    driver.get(url_to_visit)

    test_wait = WebDriverWait(driver, 120)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_to_be(url_to_visit))

    print("Successfully visited page.")

    # Functionality for checking if popup exists
    # NOTE: Maybe this can be skipped altogether

    # Find the ticket box element
    box_element = test_wait.until(EC.presence_of_element_located((By.ID, "quickpicks-listings")))

    print("Box element located.")

    # Now grab first element of this ticket box - NOTE: Should be cheapest, but this should also be asserted (when you have time)
    first_li = box_element.find_element(By.CSS_SELECTOR, "ul > li")

    # Then grab the data-price attribute of the first <li> element
    raw_price = first_li.get_attribute('data-price')

    formatted_price = price_cleanup(raw_price)

    return formatted_price

