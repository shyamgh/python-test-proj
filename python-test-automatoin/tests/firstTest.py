'''
Created on 26-Jun-2019

@author: shushangabadkar
'''

from selenium import webdriver
from tests import SeleniumBase as SB


class MyTest(SB):
    
    def f(self):
        self.getDriver().get('http://www.googl.com')

MyTest.f()