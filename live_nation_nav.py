"""Module for live nation concert nav--aka getting min ticket price"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils import price_cleanup, retry_call_until_text_is_avail


def run_livenation_min_price_check(driver: webdriver, url_to_visit: str) -> float:
    driver.get(url_to_visit)

    normal_wait = WebDriverWait(driver, 30)
    arrive_wait = WebDriverWait(driver, 10)

    arrive_wait.until(EC.url_to_be(url_to_visit))

    print("Successfully visited page.")

    # Find the ticket box element
    box_element = normal_wait.until(EC.presence_of_element_located((By.ID, "quickpicks-listings")))

    print("Box element located.")

    # Now grab second element of this ticket box - NOTE: Should be cheapest, but this should also be asserted (when you have time)
    # First <li> is a header row or something of the sort
    second_li = box_element.find_element(By.CSS_SELECTOR, "ul > li:nth-of-type(2)")

    # Then grab the data-price attribute of the second <li> element
    raw_price = second_li.get_attribute('data-price')

    if raw_price is None:
        raw_price = retry_call_until_text_is_avail(second_li, grab_attrib=True, attrib_tag="data-price")

    formatted_price = price_cleanup(raw_price)

    return formatted_price
