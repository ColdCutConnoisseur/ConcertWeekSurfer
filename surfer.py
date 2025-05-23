"""Main Price Check Runner

   1. Read config for which artists/events to price check.
   2. Categorize each event url as either TM or LN parent site.
   3. Run related price check func for particular website.
   4. Alert on ticket deals ($30 tickets)
"""

import os
import time
import random
import tempfile

import undetected_chromedriver as uc
from selenium import webdriver
from dotenv import load_dotenv

from config import check_url_dict
from live_nation_nav import run_livenation_min_price_check
from ticketmaster_nav import run_ticketmaster_min_price_check


load_dotenv()

class DriverType:
    CHROME = "chrome"
    UDC = "undetected_chrome"
    FIREFOX = "firefox"

class NoDriverException(Exception):
    pass


def categorize_url_slug(full_url: str) -> str:
    tm = "www.ticketmaster.com"
    ln = "concerts.livenation.com"

    if tm in full_url:
        return "ticketmaster"

    elif ln in full_url:
        return "livenation"

    else:
        print("Unable to categorize url!")
        return None


def create_and_return_driver(driver_type: DriverType) -> webdriver:
    if driver_type is DriverType.CHROME:
        print("Running with Chrome driver.")
        return webdriver.Chrome()

    elif driver_type is DriverType.UDC:
        print("Running with UDC driver.")

        #profile_path = os.environ["CHROME_PP"]
        profile_dir = tempfile.mkdtemp(dir="./chrome_profile")

        options = uc.ChromeOptions()

        options.add_argument(f"--user-data-dir={profile_dir}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--start-maximized")
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
    # NOTE: Alternative is that there is a driver context manager in Selenium now
    driver = create_and_return_driver(driver_type=DriverType.UDC)


    try:
        # Iterate thru configured events
        for artist, attribs in check_url_dict.items():
            
            time.sleep(random.randint(10, 20))

            print(f"Running price check for {artist}...")

            # Fork : Should run tm or ln functionality?
            event_url = attribs["url"]
            website = categorize_url_slug(event_url)

            print(f"Url categorized as {website}.")

            if website == "ticketmaster":
                min_price = run_ticketmaster_min_price_check(driver, event_url)

            elif website == "livenation":
                #min_price = run_livenation_min_price_check(driver, event_url)
                #print(min_price)
                pass

            elif website is None:
                print("Unable to categorize website as TM or LN!  Skipping...")
                continue
            
    finally:
        driver.quit()




if __name__ == "__main__":
    check_current_prices()
