'''
Created on 24-May-2018

@author: shushangabadkar

'''

from selenium.webdriver.common.keys import Keys
from base.seleniumm_base import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException
from pip._vendor.requests.exceptions import Timeout

start_driver()

init_app_with_url('http://qa1-aura.mediaocean.com/')



browser = get_driver()
timeout = 30


browser.switch_to.default_content()



try:
    element_present = EC.presence_of_element_located((By.ID, 'usernameInput'))
    WebDriverWait(browser, timeout).until(element_present)
except TimeoutException:
    print('timeout while loading login page')
    
  
element = WebDriverWait(browser, 10).until(
    lambda x: x.find_element_by_id("usernameInput"))




element.send_keys('P17025@auraauto.com')
browser.find_element_by_id('passwordInput').send_keys('Welcome1')
browser.find_element_by_id('buttonSignin').click()



clean_up()