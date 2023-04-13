from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_be_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    basket_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert basket_btn, "There is no basket button"



