import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"

chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(chrome_driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
)

time.sleep(2)
sign_in_button = driver.find_element("Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_element(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_element("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()
