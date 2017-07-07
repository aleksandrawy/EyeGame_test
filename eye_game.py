from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import wait_until


class EyeGamePage:

    url = "https://www.igame.com/eye-test/"
    def __init__(self, driver : WebDriver):   #klasa oczekuje ze dostanie instancje drivera
        self.driver = driver


    def load(self):
        self.driver.get(self.url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name('iframe'))


    def click_chosen_one(self):
        #self.driver.find_element_by_css_selector('.thechosenone').click()
        self.driver.find_element(By.CSS_SELECTOR, '.thechosenone').click()

    def get_current_time(self):
        self.driver.find_element_by_css_selector('.clock').text


    def get_to_robot_level(self):
        for i in range(30):
            self.click_chosen_one()

       # wait_until(condition=)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))

    def get_reached_level(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.character-title').text