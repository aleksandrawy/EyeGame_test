from browser import get_driver
from eye_game import EyeGamePage


def test_kret_level():
    driver = get_driver()
    eye_game = EyeGamePage(driver)
    eye_game.load()
    eye_game.get_to_robot_level()
    eye_game.check_robot_level_reached()