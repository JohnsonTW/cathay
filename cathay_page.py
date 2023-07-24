import unittest
import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from basic import BasicPage


class CathayPage(BasicPage):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = "https://www.cathaybk.com.tw/cathaybk/"

    def test_home_case(self):
        page = BasicPage(self.driver)
        try:
            page.open()
            self.wait = self.WebDriverWait(self.driver, 10)
            self.wait.until(EC.title_contains("國泰世華銀行"))
            screenshot_path = "C:/download/screenshot.jpg"
            page.get_screenshot_as_file(screenshot_path)
        except TimeoutException:
            logging.error("TimeOut for waitting the title.")
   
   
    def test_count_links(self):
        page = BasicPage(self.driver)

        try:
            self.wait = self.WebDriverWait(self.driver, 10)
            self.wait.until(EC.title_contains("國泰世華銀行"))
            screenshot_path = "C:/download/screenshot.jpg"
            page.get_screenshot_as_file(screenshot_path)
            self.menu_element = self.find_xpath("/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div")
            self.links = self.menu_element.find_elements_by_xpath('.//a')
            self.links_count = len(self.links)
            print(f'個人金融 > 產品介紹 > 信用卡列表 選單數量為:' '{self.links_count}')
        except TimeoutException:
            logging.error("TimeOut for waitting the title.")
        
        

    def test_card_compare(self):
        try:
            page = BasicPage(self.driver)
            self.html_text = page.page_source
            self.keyword = "停發卡" 
            self.keyword_count = self.html_text.count(self.keyword)
            print(f"{self.keyword } 的數量：{self.keyword_count}")
        except:
             logging.error("No match items!")

    @classmethod
    def tearDownClass(cls):
            cls.driver.quit()


if __name__ == "__main__":
     unittest.main(verbosity=2)
