import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def test_notepad_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()   

        # Open the index page
        driver.get(f'{host}/notepad')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        driver.set_window_size(1261, 939)
        driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(1)").click()
        driver.find_element(By.ID, "email").click()
        driver.find_element(By.ID, "email").send_keys("user1@example.com")
        driver.find_element(By.ID, "password").click()
        driver.find_element(By.ID, "password").send_keys("1234")
        driver.find_element(By.ID, "submit").click()
        driver.find_element(By.CSS_SELECTOR, ".content").click()

        try:
            driver.get(f'{host}/notepad/create')
            driver.find_element(By.ID, "title").click()
            driver.find_element(By.ID, "title").send_keys("CreateNotepadTest")
            driver.find_element(By.ID, "body").click()
            driver.find_element(By.ID, "body").send_keys("CreateNotepadTest")
            driver.find_element(By.ID, "submit").click()
            driver.find_element(By.LINK_TEXT, "CreateNotepadTest").click()
            driver.find_element(By.ID, "body").click()
            driver.find_element(By.ID, "body").send_keys("ShowNotepadTest")
            driver.find_element(By.ID, "submit").click()
            driver.find_element(By.LINK_TEXT, "Edit").click()
            driver.find_element(By.ID, "title").click()
            driver.find_element(By.ID, "title").send_keys("UpdateNotepadTest")
            driver.find_element(By.ID, "submit").click()
            driver.find_element(By.CSS_SELECTOR, "button").click()
            driver.find_element(By.CSS_SELECTOR, ".text-dark").click()
            driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(2)").click()          

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
test_notepad_index()
