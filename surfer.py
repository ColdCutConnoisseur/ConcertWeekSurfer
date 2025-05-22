"""Main"""


import undetected_chromedriver as uc
from selenium import webdriver





class DriverType:
    CHROME = "chrome"
    UDC = "undetected_chrome"
    FIREFOX = "firefox"

class NoDriverException(Exception):
    pass



def create_and_return_driver(driver_type: DriverType) -> webdriver:
    if driver_type is DriverType.CHROME:
        print("Running with Chrome driver.")
        return webdriver.Chrome()

    elif driver_type is DriverType.UDC:
        print("Running with UDC driver.")
        options = uc.ChromeOptions()
        #options.add_argument("--headless")  # optional
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        return uc.Chrome(options=options)

    elif driver_type is DriverType.FIREFOX:
        print("Running with FireFox driver.")
        return webdriver.Firefox()

    else:
        print(f"Following driver type not recognized: {driver_type}")
        raise NoDriverException


def check_current_prices():
    """Main loop"""
    # Setup driver
    driver = create_and_return_driver(driver_type=DriverType.UDC)



