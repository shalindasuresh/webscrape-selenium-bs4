from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options=webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver =webdriver.Firefox(executable_path=r'C:\Softwares\firefox_driver\geckodriver.exe',options=options)
driver.get("")
