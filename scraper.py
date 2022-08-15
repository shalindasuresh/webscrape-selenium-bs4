import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


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


soup = BeautifulSoup(page_source, 'lxml')
reviews = []
post_list = soup.find_all('div', class_='list-item')


for post in post_list:
   
    post_div = post.find('div', class_='dyn_full_review')
    # if review_div is None:
    #     review_div = review_selector.find('div', class_='results-list--headline-container')
   
    review = review_div.find('div', class_='results-list--headline-container').find('a').get_text()
    review = review.strip()
    reviews.append(review)


print(reviews)


