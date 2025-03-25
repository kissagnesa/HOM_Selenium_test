from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)