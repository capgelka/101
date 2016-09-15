#!/usr/bin/env python3

import sys
import os
sys.path.append(os.getcwd())

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver.locators import EXCHANGE_RATES_WIDGET



class Widget(object):

    def __init__(self):
        self.__driver = webdriver.Firefox()
        print(1)
        self.__driver.get("http://www.sberbank.ru/ru/person")
        print(2)
        WebDriverWait(self.__driver, 10).until(EC.element_to_be_clickable(EXCHANGE_RATES_WIDGET))
        self.elem = self.__driver.find_element(*EXCHANGE_RATES_WIDGET)
        print(3)

    def metals_active(self):
        print('OK')


if __name__ == '__main__':

    w = Widget()
    w.metals_active()
