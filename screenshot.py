from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

CLASS_NAME = "class name"


def get_scr(url, filename):
    # Set up options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    # Launch the Chrome browser in headless mode
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to the Reddit post
    driver.get(url)

    # Find the title element and take a screenshot of it
    title_element = driver.find_element(By.CLASS_NAME, "_eYtD2XCVieq6emjKBH3m")
    screenshot = title_element.screenshot_as_png

    # Save the screenshot as an image file
    with open(f'scr/{filename}.png', 'wb') as f:
        f.write(screenshot)

    # Close the browser
    driver.quit()

get_scr('https://www.reddit.com/r/AskReddit/comments/12dmbbk/who_is_the_worst_kind_of_person_to_be_sat_next_to/', "reddit")

