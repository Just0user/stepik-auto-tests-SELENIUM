from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    price_now = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    if price_now:
        button_book = browser.find_element_by_id('book')
        button_book.click()

    math_win = WebDriverWait(browser, 12).until(
        EC.presence_of_element_located((By.ID, 'input_value')))

    if math_win:
        x = browser.find_element_by_id('input_value').text
        y = str(math.log(abs(12*math.sin(int(x)))))

        answ = browser.find_element_by_id('answer')
        answ.send_keys(y)

        button = browser.find_element_by_id('solve')
        button.click()

    print(browser.switch_to.alert.text)
finally:
    browser.quit()

