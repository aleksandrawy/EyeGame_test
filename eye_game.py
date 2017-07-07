from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import namedtuple
from utils import wait_until

Level = namedtuple("Level", ['name', 'value'])

class EyeGamePage:

    url = "https://www.igame.com/eye-test/"

    JASTRZAB = Level(name='jastrząb', value=25)
    ROBOT = Level(name='robot', value=30)
    #ROBOT.name / ROBOT.value

    # class Levels(Enum):
    #     ROBOT = 30
    #     JASTRZAB = 25


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


    def get_to_level(self, num_of_clicks):
        for i in range(num_of_clicks):
            self.click_chosen_one()
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))


    def get_to_robot_level(self):
        self.get_to_level(self.ROBOT.value)
       #  for i in range(30):
       #      self.click_chosen_one()
       # # wait_until(condition=)
       #  WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.ID, "timeleft")))


    def get_reached_level(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.character-title').text