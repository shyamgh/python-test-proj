'''
Created on 26-Jun-2019

@author: shushangabadkar
'''

from selenium import webdriver


class SeleniumBase:

    def __init__(self):
         self._driver = webdriver.Chrome(executable_path = self.CHROME_DRIVER_PATH())
         self._driver.implicitly_wait(30)
    
    def CHROME_DRIVER_PATH(self):
        return 'C:/Development/Selenium/Drivers/chromedriver.exe'
                
    def getDriver(self):
        return self._driver