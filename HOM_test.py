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
part=driver.find_element(By.LINK_TEXT, "Regisztráció")
if part.is_displayed():
    print("Az oldal megjelenik")
else:
    print("Az oldal nem jelenik meg")
part.click()
driver.save_screenshot("Regisztracio.png")
time.sleep(5)
driver.quit