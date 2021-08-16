from selenium import webdriver

drive = webdriver.Chrome()
drive.get('https://popcat.click/')

elem = drive.find_element_by_id('app')

while True:
    elem.click()
