#%%
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('ChromeDriver/chromedriver')
driver.set_page_load_timeout(2)

try:
    driver.get("https://jewelry.ha.com/c/search-results.zx?No=204&Ne=2014&N=776+790+231+2040")
except:
    print("time out")
#%%
# get links of all rings (stored as list of lists)
URL_Links = []
Condition = True
while Condition:
    sleep(15)
    result = driver.find_elements_by_class_name('item-title')
    result = [link.get_attribute('href') for link in result]
    URL_Links.append(result)
    try:
        driver.find_element_by_xpath('//*[@id="tabs-1"]/div[3]/a[12]').click()
    except:
        condition = False
#%%
#extract list of lists into one list
URL_Link = []
for links in URL_Links:
    for link in links:
        URL_Link.append(link)
#%%
print(len(URL_Link))
#%%
#create dictionary of unique IDs and urls
ring = {'ID': a, 'URLs': URL_Link}
a = list(range(1,2256))
#%%
#convert dictionary into DataFrame
import pandas as pd
df = pd.DataFrame.from_dict(ring)
# save DataFrame as csv file
df.to_csv('urls.csv')
# %%
