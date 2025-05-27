"""This will house TM functionality"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils import price_cleanup, alert_user, element_has_text


def run_subtotal_logic_for_price(driver: webdriver, url: str, wait_object: WebDriverWait):
    # NOTE: Let's run two checks and they both have to pass

    # 1) First, is a natural price check
    price_box = wait_object.until(EC.presence_of_element_located((By.CLASS_NAME, "ticket-type-description")))

    print("Price box element found.")

    price_element = price_box.find_element(By.XPATH, "following-sibling::span")

    # Wait until the text of the span is not empty
    WebDriverWait(driver, 10).until(
        lambda d: price_element.text.strip() != ""
    )

    # Now safely grab the text
    raw_price = price_element.text.strip()

    raw_price = price_element.text

    # 2) Because the above price check might keep referencing the same element, and a new element is added for cheaper tickets,
    #   let's also assert that the len of <li> elements is what we're expecting / hasn't changed
    num_price_levels = len(driver.find_elements(By.CSS_SELECTOR, 'li[data-bdd="offer-card-ticket-item"]'))
    
    if num_price_levels != 1:
        alert_user(message="More ticket offerings available for following:\n", url=url)

    else:
        print("Expected number of offerings found.")

    return raw_price


def route_event_and_get_price(driver: webdriver, url_to_route: str, wait_object: WebDriverWait):
    """Used to handle one-off TM pages/events"""

    # One-off cases
    if "sierra-ferrell-shoot-for-the-moon-north-charleston" in url_to_route:
        raw_price = run_subtotal_logic_for_price(driver, url_to_route, wait_object)

        formatted_price = price_cleanup(raw_price)

        return formatted_price

    # Normal flow of operations
    else:

        # Find the ticket box element
        box_element = wait_object.until(EC.presence_of_element_located((By.ID, "quickpicks-listings")))

        print("Box element located.")

        """ Replaced by fancy GPT below
        # Now grab first element of this ticket box - NOTE: Should be cheapest, but this should also be asserted (when you have time)
        first_li = box_element.find_element(By.CSS_SELECTOR, "ul > li")

        # Then grab the data-price attribute of the first <li> element
        raw_price = first_li.get_attribute('data-price')
        """

        first_li = WebDriverWait(box_element, 10).until(
            lambda d: box_element.find_element(By.CSS_SELECTOR, "ul > li")
        )

        # 2. Wait until that <li> has non-empty text (or use .textContent if necessary)
        WebDriverWait(driver, 10).until(
            lambda d: first_li.text.strip() != ""
        )

        # 3. Now it’s safe to get the price attribute or display text
        raw_price = first_li.get_attribute("data-price")

        formatted_price = price_cleanup(raw_price)

        return formatted_price



def run_ticketmaster_min_price_check(driver: webdriver, url_to_visit: str) -> float:
    driver.get(url_to_visit)

    normal_wait = WebDriverWait(driver, 25)
    arrive_wait = WebDriverWait(driver, 10)
    
    arrive_wait.until(EC.url_to_be(url_to_visit))

    print("Successfuly visited page.")

    route_event_and_get_price(driver, url_to_visit, normal_wait)


