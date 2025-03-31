import add_path
import pytest
import mit_ocw_data_science.lec2.menu.py as lec2
import random

def test_food():
    # 測試 Food 類別的基本功能
    food = lec2.Food("apple", 50, 95)
    assert food.get_value() == 50
    assert food.get_cost() == 95
    assert food.density() == pytest.approx(50 / 95)
    assert str(food) == "apple: <50, 95>"

def test_menu():
    # 測試 Menu 類別的基本功能
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [95, 105, 120]
    menu = lec2.Menu(names, values, calories)

    # 測試 get_foods 方法
    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(foods[0]) == "apple: <50, 95>"
    assert str(foods[1]) == "banana: <60, 105>"
    assert str(foods[2]) == "cherry: <70, 120>"

    # 測試 __str__ 方法
    assert str(menu) == "apple: <50, 95>; banana: <60, 105>; cherry: <70, 120>; "


