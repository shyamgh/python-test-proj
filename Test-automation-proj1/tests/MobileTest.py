'''
Created on 30-Sep-2019

@author: shushangabadkar
'''
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base.seleniumm_base import driver
from win32api import GetDateFormat
from asn1crypto._ffi import null


class Test(unittest.TestCase):
    
    driver
    
    def initDriver(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0',
            'deviceName': 'Android Emulator',
            'udid' : 'emulator-5554',
            'browserName': 'Chrome'
        }
        self.setDriver(desired_caps)
    
    def setDriver(self, desired_caps):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def getDriver(self):
        return self.driver        
    
    def setUp(self):
        self.initDriver()

    def tearDown(self):
        if self.driver is not None:
            self.driver.close()
        self.driver = None
            
    def launchGoogle(self):
        self.driver = self.getDriver()
        self.driver.get("https://www.google.com")
        
    def testSearchElement(self):
        self.launchGoogle()
        element = driver.find_element_by_class_name('q')
        assert element.is_displayed()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()