"""Various helper functions"""

from selenium.webdriver.support.ui import WebDriverWait

def wait_for_nonempty_text(driver, element, timeout=10):
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
