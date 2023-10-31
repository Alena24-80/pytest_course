import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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


# def test_dropdown(driver, login):
#     driver.find_element(By.CSS_SELECTOR, '.select_container').click()
#     time.sleep(3)
#     driver.find_element(By.CSS_SELECTOR, '.select_container option:nth-child(3)').click()
#     time.sleep(10)
#     select = Select(driver.find_element(By.CSS_SELECTOR, '.product_sort_container'))
#     time.sleep(1)
#     select.select_by_value('lohi')
#     time.sleep(10)

"""Проверка работоспособности фильтра (A to Z)"""
def test_check_filter_A_to_Z(driver, login):
    driver.find_element(By.CSS_SELECTOR, '.select_container').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.select_container option:nth-child(1)').click()
    time.sleep(10)
    select = Select(driver.find_element(By.CSS_SELECTOR, '.product_sort_container'))
    time.sleep(1)
    select.select_by_value('az')
    time.sleep(10)


"""Проверка работоспособности фильтра (Z to A)"""
def test_check_filter_Z_to_A(driver, login):
    sort_before = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
    item_lst_before = []
    for i in sort_before:
        item_lst_before.append(i.text)
    item_lst_before.sort(reverse=True)
    driver.find_element(By.CSS_SELECTOR, '.select_container').click()
    driver.find_element(By.CSS_SELECTOR, '.select_container option:nth-child(2)').click()
    sort_after = driver.find_elements(By.CSS_SELECTOR, '.inventory_item_name')
    item_lst_after = []
    for i in sort_after:
        item_lst_after.append(i.text)

    assert item_lst_before == item_lst_after

"""Проверка работоспособности фильтра (low to high)"""
def test_check_filter_low_to_high(driver, login):
    driver.find_element(By.CSS_SELECTOR, '.select_container').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.select_container option:nth-child(3)').click()
    time.sleep(10)
    select = Select(driver.find_element(By.CSS_SELECTOR, '.product_sort_container'))
    time.sleep(1)
    select.select_by_value('lohi')
    time.sleep(10)
    cart = Select(driver.find_element(By.XPATH, '//select[@class="product_sort_container"]'))

    assert cart


"""Проверка работоспособности фильтра (high to low)"""
def test_check_filter_high_to_low():
