import time
from selenium import webdriver

# 웹 드라이버 설정
driver = webdriver.Chrome(r"C:\Program Files\chromedriver.exe")
driver.implicitly_wait(3)

driver.get('https://workey.codeit.kr/costagram/index')
time.sleep(5)

driver.maximize_window()
time.sleep(2)



driver.find_element_by_css_selector('.top-nav__login-link').click()
time.sleep(1)

driver.find_element_by_css_selector('.login-container__login-input').send_keys('codeit')
driver.find_element_by_css_selector('.login-container__password-input').send_keys('datascience')

driver.find_element_by_css_selector('.login-container__login-button').click()
time.sleep(1)




last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


driver.quit()