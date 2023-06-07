import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import re
from functions import *
import requests
import os

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service("chromedriver.exe"), options=chrome_options)
url = "https://www.caricos.com/cars/"
car_page = "https://www.caricos.com/cars/"

p_911_gt3_rs = "https://www.caricos.com/cars/p/porsche/2023_porsche_911_gt3_rs/"
x6m = "https://www.caricos.com/cars/b/bmw/2024_bmw_x6_m_competition/"
defender = "https://www.caricos.com/cars/l/land_rover/2022_land_rover_defender_v8_110/"
m340i = "https://www.caricos.com/cars/b/bmw/2023_bmw_m340i/"


driver.get(m340i)

folder_name = "M340i"

payload={}
headers = {
  'Referer': 'https://www.caricos.com/',
  'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

all_valid_images = []

for each in get_all_href(driver):
    if re.match(r"https://images.caricos.com", each.get_attribute("href")):
        all_valid_images.append(each.get_attribute("href"))


print(all_valid_images)


time.sleep(5)
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for url in all_valid_images:
    response = requests.get(url, headers=headers, data=payload)
    filename = os.path.join(folder_name, os.path.basename(url))
    with open(filename, "wb") as f:
        f.write(response.content)






