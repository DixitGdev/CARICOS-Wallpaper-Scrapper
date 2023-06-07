from selenium.common import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_all_makes(driver):
    All_makes = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'allmakes')))
    return All_makes.text


def get_all_href(driver):
    all_href = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "modelimgviewimg")))
    return all_href
