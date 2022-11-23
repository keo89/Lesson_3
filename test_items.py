import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestFindBasket():

    def test_PutInBasket(self, browser):
        browser.get(link)
        button = len(browser.find_elements(By.CSS_SELECTOR, "[value= 'Добавить в корзину']"))
        assert button > 0, 'Не найдена корзина'

