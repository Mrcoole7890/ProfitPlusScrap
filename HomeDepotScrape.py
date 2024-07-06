from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


load_dotenv()


TIME_TO_SLEEP = int(os.getenv('TIME_TO_SLEEP'))
STORE_FINDER_URL = os.getenv('STORE_FINDER_URL')
STORE_NUMBER = os.getenv('STORE_NUMBER')
XPATH_TO_STORE_SEARCH_BAR = os.getenv('XPATH_TO_STORE_SEARCH_BAR')
XPATH_TO_FIRST_STORE_CARD = os.getenv('XPATH_TO_FIRST_STORE_CARD')
XPATH_TO_SEARCHBAR = os.getenv("XPATH_TO_SEARCHBAR")
DRIVER_WAIT_TIME = int(os.getenv('DRIVER_WAIT_TIME'))
XPATH_TO_SHOP_ALL_BUTTON = os.getenv('XPATH_TO_SHOP_ALL_BUTTON')
XPATH_TO_SHOP_BY_DEPARTMENT_OPTION = os.getenv('XPATH_TO_SHOP_BY_DEPARTMENT_OPTION')
XPATH_TO_SHOP_BY_TILES_OPTION = os.getenv('XPATH_TO_SHOP_BY_TILES_OPTION')
XPATH_TO_SHOP_BY_FLOOR_TILES_OPTION = os.getenv('XPATH_TO_SHOP_BY_FLOOR_TILES_OPTION')
XPATH_TO_SHOP_BY_FLOORING_TILES_RUGS_OPTION = os.getenv('XPATH_TO_SHOP_BY_FLOORING_TILES_RUGS_OPTION')
XPATH_TO_IN_STORE_RESULTS = os.getenv('XPATH_TO_IN_STORE_RESULTS')
XPATH_TO_GRID = os.getenv('XPATH_TO_GRID')

driver = webdriver.Chrome()
wait = WebDriverWait(driver, DRIVER_WAIT_TIME)

driver.get(STORE_FINDER_URL)

store_search_bar = driver.find_element(By.XPATH, XPATH_TO_STORE_SEARCH_BAR)
store_search_bar.send_keys(STORE_NUMBER)
store_search_bar.send_keys(Keys.ENTER)

store_to_select = driver.find_element(By.XPATH, XPATH_TO_FIRST_STORE_CARD)
store_to_select.find_element(By.XPATH, XPATH_TO_FIRST_STORE_CARD + "//button").click()

driver.refresh()

shop_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_TO_SHOP_ALL_BUTTON)))
shop_all_button.click()
shop_by_department_button = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_TO_SHOP_BY_DEPARTMENT_OPTION)))
shop_by_department_button.click()
shop_by_floor_tiles_rugs_button = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_TO_SHOP_BY_FLOORING_TILES_RUGS_OPTION)))
shop_by_floor_tiles_rugs_button.click()
shop_by_tiles_button =  wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_TO_SHOP_BY_TILES_OPTION)))
shop_by_tiles_button.click()
shop_by_floor_tiles_button = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_TO_SHOP_BY_FLOOR_TILES_OPTION)))
shop_by_floor_tiles_button.click()
refine_results_to_in_store_button = wait.until(EC.element_to_be_clickable((By.XPATH, XPATH_TO_IN_STORE_RESULTS)))
refine_results_to_in_store_button.click()

grid = wait.until(EC.visibility_of_element_located((By.XPATH, XPATH_TO_GRID)))

sections = wait.until(EC.presence_of_all_elements_located((By.XPATH, XPATH_TO_GRID + "//section[@class='grid']")))

for section in sections:
    print(section.text)

time.sleep(TIME_TO_SLEEP)

