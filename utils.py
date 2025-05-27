"""Various helper functions"""

import time

from selenium.webdriver.support.ui import WebDriverWait



def retry_call_until_text_is_avail(element, grab_attrib=False, attrib_tag=None):
    # TODO:  This can be replaced with something way cleaner; I'm just trying to get this workflow going at this point
    max_retries = 10
    timeout = 2
    retries = 0

    while True:
        if retries >= max_retries:
            print("Max timeout hit.")
            return None

        time.sleep(timeout)

        if grab_attrib:
            fetched = element.get_attribute(attrib_tag)

        else:
            fetched = element.text.strip()

        if fetched is not None:
            return fetched

        retries += 1

def DEPRwait_for_nonempty_text(driver, element, timeout=10):
    """
    Waits until an element's .text or .textContent is non-empty.
    Returns the resolved text once available.
    """
    def _has_text(_):
        # First try Selenium's .text
        text = element.text.strip()
        if text:
            return text

        # Fallback to JS .textContent
        text = driver.execute_script("return arguments[0].textContent.trim()", element)
        return text if text else False

    return WebDriverWait(driver, timeout).until(_has_text)

def price_cleanup(raw_price: str) -> float:
    # Remove '$' char
    no_sign = str(raw_price).replace('$', '')
    print(f"After replace --> {no_sign}")
    as_float = float(no_sign)
    return as_float


def alert_user(message: str, url: str):
    print("TODO: create alert_user callback!")
