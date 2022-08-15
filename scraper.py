import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup



def main()->webdriver: 
    options=webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver =webdriver.Firefox(executable_path=r'C:\Softwares\firefox_driver\geckodriver.exe',options=options)
    driver.get("https://www.businessoffashion.com/news/")
    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.END)
    
    return driver

def find_visible_more_buttons(driver):

    more_buttons = driver.find_elements(By.CLASS_NAME,"iugaRF")
    
    if(len(more_buttons)>0):
        do_click_more_buttons(driver,more_buttons)
    else:
        do_scrape_data(driver)
        
    
    
def do_click_more_buttons(driver,more_buttons):
    time.sleep(2)
    for x in range(len(more_buttons)):
        if more_buttons[x].is_displayed():
            print("Clicking more button")
            driver.execute_script("arguments[0].click();", more_buttons[x])
           
    find_visible_more_buttons(driver)
    

def do_scrape_data(driver):
    
    print("Scraping data")
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    reviews = []
    post_list = soup.find_all('div', class_='list-item')
    post_div = post.find('div', class_='dyn_full_review')
    # if review_div is None:
    #     review_div = review_selector.find('div', class_='results-list--headline-container')
   
    review = review_div.find('div', class_='results-list--headline-container').find('a').get_text()
    review = review.strip()
    reviews.append(review)
    print(reviews)
    

if __name__ == '__main__' :
     driver=main()
     find_visible_more_buttons(driver)
    

