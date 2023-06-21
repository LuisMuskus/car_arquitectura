# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random

class ScrapCourses():
    def setUp():
        pass

    def test_scrap_courses():
        items=10
        i=0
        try:
            driver = webdriver.Chrome()
            driver.implicitly_wait(30)
            base_url = "https://www.google.com/"
            list_data= []
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get("https://www.aulafacil.com/")
            driver.maximize_window()
            time.sleep(5)

        except:
            print("Hay un error con la configuracion del driver Chrome")
            driver.quit()

        try:
            while i<3:
                item_course = random.randint(1, 16)
                if item_course == 1:
                    info_course=driver.find_element(By.XPATH, "//div[@id='secc-principal']/section/div/div[2]/div[2]/div[2]/section/main/div/div/div").text
                    split_course=info_course.split("\n")
                else:
                    info_course=driver.find_element(By.XPATH, "//div[@id='secc-principal']/section/div/div[2]/div[2]/div[2]/section/main/div/div["+str(item_course)+"]/div").text
                    split_course=info_course.split("\n")
                list_data.append(split_course)
                time.sleep(3)

                i=i+1
        except NoSuchElementException as e:
            print ("Hubo un error al cargar un selector...")
            driver.quit()
        df = pd.DataFrame(list_data, columns =["name_course", "description_course"])
        print(df)
        df.to_excel('scrap_cursos.xlsx')
        time.sleep(3)
        driver.quit()

#nuevo=ScrapCourses.test_scrap_courses()
