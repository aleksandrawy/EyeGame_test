from selenium.webdriver import Firefox


def get_driver():
    driver = Firefox()
    driver.implicitly_wait(5) #czeka 5 sek jesli nic nie znalazl
    return driver