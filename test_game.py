# -*- coding: utf-8 -*-

from eye_game import EyeGamePage
from collections import namedtuple
import pytest

Level = namedtuple("Level", ['name', 'value'])

JASTRZAB = Level(name='JASTRZĄB', value=25)
ROBOT = Level(name='ROBOT', value=30)

# def test_exception():
#     assert False

@pytest.mark.parametrize("level", [JASTRZAB, ROBOT])
def test_levels(driver, level):
    #driver = get_driver()
    eye_game = EyeGamePage(driver)
    eye_game.load()
    eye_game.get_to_level(level=level)
    eye_game.check_level_reached(level=level)

@pytest.mark.smoke_test
def test_title(driver):

    eye_game = EyeGamePage(driver)
    eye_game.load()
    assert "Eye" in eye_game.get_title()