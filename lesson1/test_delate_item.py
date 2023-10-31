from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



def test_login_form():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

    driver.quit()

"""Удаление товара из корзины через корзину"""

def test_delate_item():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)

    backpack_link = driver.find_element(By.XPATH, '//div[text()="Sauce Labs Backpack"]')
    backpack_link.click()

    time.sleep(5)

    add_button = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_button.click()

    time.sleep(5)

    remove_button = driver.find_element(By.CSS_SELECTOR, '#remove-sauce-labs-backpack')
    remove_button.click()

    time.sleep(5)


    anable_button = driver.find_element(By.CSS_SELECTOR, '.inventory_details_desc_container button')

    assert anable_button.text == 'Add to cart'
