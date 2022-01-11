import time
import math
from math import *
from selenium import webdriver


def calc(x):
    return str(log (abs(12 * sin(x))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = x_element.text
    y = calc(int(x))
    input1 = browser.find_element_by_xpath("//input[@id='answer']")
    input1.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("window.scrollBy(0, 150);",button)
    check_box_1 = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    check_box_1.click()
    radio_check1 = browser.find_element_by_xpath("//input[@value='robots']")
    radio_check1.click()
    button_sub1 = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    button_sub1.click()
finally:
    time.sleep(30)
    browser.quit()
