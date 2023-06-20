#from django.test import TestCase
import unittest

# Create your tests here.

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from selenium.webdriver.common.by import By
import time
import pandas as pd

class ScrapCourses(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_scrap_courses(self):
        list_data= []
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        driver = self.driver
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.aulafacil.com/")
        driver.maximize_window()
        time.sleep(5)
        a=driver.find_element(By.XPATH, "//div[@id='secc-principal']/section/div/div[2]/div[2]/div[2]/section/main/div/div/div").text
        split_a=a.split("\n")
        #print(split_a)
        list_data.append(split_a)
        time.sleep(3)
        b=driver.find_element(By.XPATH, "//div[@id='secc-principal']/section/div/div[2]/div[2]/div[2]/section/main/div/div[2]/div").text
        split_b=b.split("\n")
        #print(split_b)
        list_data.append(split_b)
        time.sleep(3)
        c= driver.find_element(By.XPATH, "//div[@id='secc-principal']/section/div/div[2]/div[2]/div[2]/section/main/div/div[3]/div").text
        split_c=c.split("\n")
        #print(split_c)
        list_data.append(split_c)
        time.sleep(3)
        #print(list_data)
        df = pd.DataFrame(list_data, columns =["name_course", "description_course"])
        print(df)
        df.to_excel('scrap_cursos.xlsx')
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
