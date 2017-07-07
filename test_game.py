from browser import get_driver
from eye_game import EyeGamePage


def test_kret_level():
    driver = get_driver()
    eye_game = EyeGamePage(driver)
    eye_game.load()
    #eye_game.click_chosen_one()
    eye_game.get_to_robot_level()
    assert eye_game.get_reached_level() == 'ROBOT'