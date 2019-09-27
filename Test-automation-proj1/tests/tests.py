'''
Created on 24-May-2018

@author: shushangabadkar

'''

from selenium.webdriver.common.keys import Keys
from base.seleniumm_base import *


start_driver()
init_app()

browser = get_driver()

browser.find_element_by_name('q').send_keys('using webdriver with python + eclipse')

browser.find_element_by_name('q').send_keys(Keys.ENTER)

clean_up()