'''
Created on 26-Jun-2019

@author: shushangabadkar
'''
import unittest
from tests.SeleniumBase import SeleniumBase as SB
from tests.GoogleSearchPage import GoogleSearchPage




class Test(unittest.TestCase):

    def test_1(self):
        driver = SB().getDriver()
        driver.get('https://www.google.com')
        list1 = driver.find_elements_by_name('q')
        print(list1[0].get_attribute('name'))
        
        '''
        gspage = GoogleSearchPage(driver)
        gspage._search_box = 'hello'
        gspage._search_box.click()
        gspage._belowLinks.is_
        '''
        
        gspage = GoogleSearchPage(driver)
        gspage.search_box().send_keys('hello')
        gspage.search_box().submit()
        gspage.below_links().is_displayed()
        
        
        driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()