'''
Created on 24-May-2018

@author: shushangabadkar

'''

from selenium import webdriver


driver = None

def start_driver():
    global driver 
    driver = webdriver.Chrome('C:\Development\Selenium\Drivers\chromedriver.exe')
    #driver = webdriver.Ie('C:\Development\Selenium\Drivers\IEDriverServer.exe')
    return driver
    
def clean_up():
    global driver
    driver.quit()

def init_app():
    global driver
    driver.get('https://www.google.com')
    
def init_app_with_url(url):
    global driver
    driver.get(url)
    
def get_driver():
    global driver
    return driver