from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)

driver.get("https://rejtelyekhaza.netlify.app/")
driver.save_screenshot("HOM_test.png")
time.sleep(5)
part=driver.find_element(By.LINK_TEXT, value="Bejelentkezés")
part.click()
driver.save_screenshot("Bejelentkezes.png")
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('sindzse88@gmail.com')
time.sleep(1)
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('teszt')
time.sleep(1)
driver.find_element(By.TAG_NAME, 'button').click()
driver.save_screenshot('first_login.png')
time.sleep(1)
time.sleep(5)
driver.quit