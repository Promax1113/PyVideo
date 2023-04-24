import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

CLASS_NAME = "class name"


def get_post_scr(url, filename):
    # Set up options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Launch the Chrome browser in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the Reddit post
    driver.get(url)
    time.sleep(2)
    # Find the title element and take a screenshot of it
    title_element = driver.find_element(By.CSS_SELECTOR, F"#thing_t3_{filename} > div.entry.unvoted > div > p.title > a")
    screenshot = title_element.screenshot_as_png

    # Save the screenshot as an image file
    with open(f'scr/{filename}.png', 'wb') as f:
        f.write(screenshot)

    # Close the browser
    driver.quit()

# The comment screenshotter is hard to use.


def get_comment_screenshot(url, post_id):
    # Set up options for headless browsing
    del_cookies = False
    iterations = 0
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Launch the Chrome browser in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the Reddit post
    driver.get(url)
    time.sleep(4)
    if not del_cookies:
        del_cookies = True
        driver.find_element(By.CSS_SELECTOR, "div#SHORTCUT_FOCUSABLE_DIV > div:nth-of-type(3) > div > section > div > section:nth-of-type(2) > section > form > button").click()
    else:
        pass
    comments = driver.find_elements(By.CLASS_NAME, "_1qeIAgB0cPwnLhDF9XSiJM")
    for comment in comments:
        if iterations <= 3:
            break
        # Find the comment element and take a screenshot of it But still waiting for cookie banner animation to end.
        time.sleep(1)
        screenshot = comment.screenshot_as_png

        # Save the screenshot as an image file
        with open(f'scr/comments/{post_id}_{iterations}.png', 'wb') as f:
            f.write(screenshot)

    # Close the browser
    driver.quit()
