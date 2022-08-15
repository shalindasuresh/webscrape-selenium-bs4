import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver =webdriver.Firefox(executable_path=r'C:\Softwares\firefox_driver\geckodriver.exe',options=options)
driver.get("https://www.businessoffashion.com/news/")


initiate=True


def find_visible_more_buttons():
    

    more_buttons = driver.find_elements(By.CLASS_NAME,"iugaRF")
    print(len(more_buttons))
    if(len(more_buttons)>0):
        do_click_more_buttons(more_buttons)
    else:
           print("No more buttons to click")

def do_click_more_buttons(more_buttons):
    for x in range(len(more_buttons)):
        if more_buttons[x].is_displayed():
            driver.execute_script("arguments[0].click();", more_buttons[x])
            time.sleep(1)
    time.sleep(2)
    find_visible_more_buttons()
    
    
if(initiate):
    initiate=False
    find_visible_more_buttons()
      
print("Scraping started")
page_source = driver.page_source
