import pyperclip
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from css_selectors import selectors
import subprocess

from collections import deque

reel_url_queue = deque()


def add_reels_to_queue(username: str, password: str, num_reels: int = 100) -> None:
    try:
        # driver setup

        options = uc.ChromeOptions()
        options.add_argument("--headless")
        driver = uc.Chrome()
        instagram_url = "https://www.instagram.com/accounts/login/?__coig_restricted=1"
        driver.get(instagram_url)

        wait = WebDriverWait(driver=driver, timeout=3000)
        get_url = driver.current_urle
        wait.until(EC.url_to_be(instagram_url))

        if get_url == instagram_url:
            # I imagine this has something to do with cookies, so a note for the future
            # Note: either use or remove
            '''
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, features="html.parser")
            '''

            # wait until login page is located
            wait.until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="loginForm"]/div/div[1]/div/label/input')
                )
            )

            username_field = driver.find_element(
                by=By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input'
            )
            password_field = driver.find_element(
                by=By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input'
            )

            username_field.send_keys(username)
            password_field.send_keys(password)

            login_button = driver.find_element(
                by=By.XPATH, value='//*[@id="loginForm"]/div/div[4]'
            )
            login_button.submit()

            wait.until(EC.url_to_be(
                "https://www.instagram.com/accounts/onetap/?next=%2F"))

            reels_url = "https://www.instagram.com/reels/?next=%2F"
            driver.get(reels_url)
            wait.until(EC.url_to_be(reels_url))

            # Loop over reels
            for reel_num in range(num_reels):
                wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, selectors["more_button"](reel_num))
                    )
                )
                more_button = driver.find_element(
                    by=By.CSS_SELECTOR, value=selectors["more_button"](
                        reel_num)
                )
                more_button.click()

                wait.until(
                    EC.element_to_be_clickable(
                        (By.CSS_SELECTOR, selectors["copy_link"]))
                )
                copy_button = driver.find_element(
                    by=By.CSS_SELECTOR, value=selectors["copy_link"]
                )
                copy_button.click()

                reel_url = pyperclip.paste()
                print(f"Reel {reel_num} link: {reel_url}")
                reel_url_queue.append(reel_url)

            driver.quit()

    except Exception as e:
        print(f"An error occurred: {e}")

        # Run script2.py
        subprocess.run(['python3', 'error_emailer.py'])
        driver.quit()


if __name__ == "__main__":
    add_reels_to_queue(username="burner3deniz1",
                       password="q1.w2.e3.", num_reels=10000)
    print("\n\nURL Queue:\n", reel_url_queue)
    try:
        with open('example.txt', 'w') as file:
            # Write some text to the file
            file.write(reel_url_queue)

    except:
        subprocess.run(['python3', 'error_emailer.py'])
        print("DEBUG: error")
