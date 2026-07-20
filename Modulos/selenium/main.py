from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def make_chrome_browser(*options):
    chrome_options = webdriver.ChromeOptions()

    for option in options:
        chrome_options.add_argument(option)

    browser = webdriver.Chrome(
        options=chrome_options
    )

    return browser


if __name__ == "__main__":
    TIME_TO_WAIT = 10
    browser = make_chrome_browser(
        # "--headless",
        # "--disable-gpu",
    )

    browser.get("https://google.com")
    #Espere para encontrar o imput
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME,'q')
        )
    )
    search_input.send_keys('Hello World')#envia teclas send_keys
    search_input.send_keys(Keys.ENTER)#envia teclas send_keys

    #Dorme por 10 seconds
    sleep(TIME_TO_WAIT)
    
# forma nova
# from selenium import webdriver

# options = webdriver.ChromeOptions()

# options.add_argument("--incognito")
# options.add_argument("--start-maximized")

# driver = webdriver.Chrome(options=options)