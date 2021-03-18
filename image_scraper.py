#%%
from selenium import webdriver
from time import sleep
import requests
import os
import io
from PIL import Image
import hashlib
import json

driver = webdriver.Chrome('ChromeDriver/chromedriver')
driver.set_page_load_timeout(2)
image_src = []

try:
    driver.get("https://jewelry.ha.com/c/search-results.zx?N=776+790+231+2040&Ne=2014&erpp=204")
except:
    print("time out")

def get_ring_url():
    with open('url.json') as json_file:
        url_from_json_file = json.load(json_file)
    url_link = url_from_json_file['links']
    return url_link

def download_file(src_url, folder_path, number):
    image_content = requests.get(src_url).content
    image_file = io.BytesIO(image_content)
    image = Image.open(image_file).convert('RGB')
    file_path = os.path.join(folder_path, 'photo'+ str(number) + '.jpg')
    print(file_path)
    with open(file_path, 'wb') as f:
        image.save(f, "JPEG", quality=85)
        print(f"SUCCESS")

url = get_ring_url()
#%%
for ixd, link in enumerate(url):
    try:
        driver.get(link)
        sleep(15)
    except:
        print('TIME OUT')
    try:
        img_src = driver.find_element_by_xpath('//*[@id="page-content"]/div/div[5]/div[1]/div[3]/div/div/div[1]/div[1]/span[1]/img').get_attribute('data-high-image-src')
    except:
        pass
    number=ixd
    image_src.append(img_src)
    download_file(img_src, '..\Diamond_Rings_data\images', number)

# %%
