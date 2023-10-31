import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# driver = webdriver.Chrome()

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

"""Успешный переход к карточке товара после клика на картинку товара"""

def test_positive_input_item_cart_picture(driver, login):
    push_picture = driver.find_element(By.XPATH, '//a[@id="item_4_img_link"]')
    push_picture.click()
    time.sleep(5)

    check_cart = driver.find_element(By.CSS_SELECTOR, '.inventory_details_img_container')
    time.sleep(5)

    assert check_cart




"""Успешный переход к карточке товара после клика на название товара"""

def test_positive_input_item_cart_name(driver, login):
    text_before = driver.find_element(By.XPATH, '//a[@id="item_5_title_link"]').text
    push_button = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Fleece Jacket"]')
    push_button.click()
    time.sleep(5)

    text_after = driver.find_element(By.CSS_SELECTOR, '.inventory_details_name.large_size').text
    time.sleep(5)
    assert text_before == text_after
