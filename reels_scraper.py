from collections import deque

import pyperclip
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from css_selectors import selectors

# TODO: Save cookies to prevent account from getting banned
# cookies = driver.get_cookies()
# print("Saving cookies")
# with open('./cookies.txt', 'w') as f:
#     for cookie in cookies:
#         f.write(f"{cookie['name']}={cookie['value']};\n")

# print("Cookies saved")

# with open('./cookies.txt', 'r') as f:
#     for line in f:

#         cookie = {}
#         name, value = line.strip().split('=', 1)
#         cookie['name'] = name
#         cookie['value'] = value
#         driver.add_cookie(cookie)

reel_url_queue = deque()


def add_reels_to_queue(username: str, password: str, num_reels: int = 100) -> None:
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
                (By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
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
                by=By.CSS_SELECTOR, value=selectors["more_button"](reel_num)
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


if __name__ == "__main__":
    add_reels_to_queue(username="burner3deniz1",
                       password="q1.w2.e3.", num_reels=10)
    print("\n\nURL Queue:\n", reel_url_queue)
