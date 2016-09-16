#!/usr/bin/env python3

import sys
import os
sys.path.append(os.getcwd())

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from driver.locators import WIDGET_PARENT, EXCHANGE_RATES_WIDGET



class WidgetsFrame(object):

    def __init__(self):
        self.__driver = webdriver.Firefox()
        print(1)
        self.__driver.get("http://www.sberbank.ru/ru/person")
        print(2)
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(WIDGET_PARENT))
        # import time
        # time.sleep(10)
        self.elem = self.__driver.find_element(*WIDGET_PARENT)
        print(3)

    def metals_active(self):
        print('OK')


    def __del__(self):
        self.__driver.close()


if __name__ == '__main__':

    w = WidgetsFrame()
    w.metals_active()
#\33 1dd528b-7614-4ccf-b6c2-087cd5f1b821

# InvalidSelectorError: Compound class names not permitted
