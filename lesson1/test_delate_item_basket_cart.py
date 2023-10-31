from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

"""Удаление товара из корзины через карточку товара"""

def test_delate_item_basket_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    text_before = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light').text
    #
    # time.sleep(5)
    #
    push_button = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    push_button.click()
    time.sleep(5)

    add_button = driver.find_element(By.XPATH,'//a[@id="item_0_title_link"]')
    add_button.click()
    # basket = driver.find_element(By.CSS_SELECTOR, 'a[class="shopping_cart_link"]')
    # basket.click()
    time.sleep(5)
    remove_button = driver.find_element(By.XPATH,'//button[@id="remove-sauce-labs-bike-light"]')
    remove_button.click()

    time.sleep(5)


    text_after = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light').text
    time.sleep(5)
    assert text_before == text_after

