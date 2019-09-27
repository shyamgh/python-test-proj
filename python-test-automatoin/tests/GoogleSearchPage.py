'''
Created on 26-Jun-2019

@author: shushangabadkar
'''

from page_objects import PageObject, PageElement
from tests.SeleniumBase import SeleniumBase
#import cacheable, callable_find_by as find_by
from selenium.webdriver.common.by import By

class GoogleSearchPage():
    
    _driver = None
    
    def __init__(self, driver):
        self._driver = driver
    
    def search_box(self):
        return self._driver.find_element_by_name('q')
    
    #_belowLinks = PageElement(id='hdtbSum')
        
    def below_links(self):
        return self._driver.find_element_by_id('hdtbSum')