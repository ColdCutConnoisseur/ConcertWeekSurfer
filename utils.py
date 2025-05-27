"""Various helper functions"""


def element_has_text(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return element.text.strip() != ""
    return _predicate

def price_cleanup(raw_price: str) -> float:
    # Remove '$' char
    no_sign = str(raw_price).replace('$', '')

    as_float = float(no_sign)

    return as_float


def alert_user(message: str, url: str):
    print("TODO: create alert_user callback!")
