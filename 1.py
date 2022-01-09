#성공
from selenium import webdriver

driver = webdriver.Chrome(r"D:\바탕화면\chromedriver.exe")
driver.implicitly_wait(3)

driver.get('https://www.instagram.com/')


driver.find_element_by_css_selector('#loginForm > div > div:nth-child(1) > div > label > input').send_keys('01051932867')
driver.find_element_by_css_selector('#loginForm > div > div:nth-child(2) > div > label > input').send_keys('kdh493200!I')

driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div').click()