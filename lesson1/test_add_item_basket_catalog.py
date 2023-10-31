from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""Добавление товара в корзину через каталог"""

def test_add_item_basket_catalog():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Bolt T-Shirt"]').text

    time.sleep(5)

    add_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    add_button.click()
    time.sleep(5)

    basket = driver.find_element(By.CSS_SELECTOR, 'a[class = "shopping_cart_link"]')
    basket.click()

    text_after = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Bolt T-Shirt"]').text
    time.sleep(5)
    assert text_before == text_after

