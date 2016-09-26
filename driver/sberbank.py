#!/usr/bin/env python3

import sys
import os
sys.path.append(os.getcwd())

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from selenium.webdriver.support.ui import WebDriverWait

import driver.locators as L


def ajax_complete(driver):
    try:
        return 0 == driver.execute_script("return jQuery.active")
    except WebDriverException:
        pass

class WidgetFrame(object):

    def __init__(self):
        self.__driver = webdriver.Firefox()
        self.__driver.get("http://www.sberbank.ru/ru/person")
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(L.WIDGET_PARENT))
        WebDriverWait(self.__driver, 10).until(ajax_complete, "Timeout waiting for page to load")

    def _element_exists(self, selector, value):
        try:
            self.__driver.find_element(by=selector, value=value)
        except NoSuchElementException:
            return False
        else:
            return True


    def click_metals(self):
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(L.METALS_BUTTON))
        self.__driver.find_element(*L.METALS_BUTTON).click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(L.METALS_BUTTON))


    def metals_active(self):
        WebDriverWait(self.__driver, 10).until(ajax_complete, "Timeout waiting for page to load")
        return self._element_exists(*L.PALLADIUM)

    def click_info(self):
        info = L.DOLLAR_INFO if not self.metals_active else L.METAL_INFO
        logo = L.NEW_LOGO if not self.metals_active else L.METAL_LOGO
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(info))
        self.__driver.find_element(*info).click()
        WebDriverWait(self.__driver, 10).until(EC.presence_of_element_located(logo))
        WebDriverWait(self.__driver, 10).until(ajax_complete, "Timeout waiting for page to load")


    def close(self):
        self.__driver.quit()

    @property
    def url(self):
        return self.__driver.current_url