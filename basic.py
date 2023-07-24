import time

class BasicPage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url = None):
        if url is None:
            self.driver.get(self,url)
        else:
            self.driver.get(url)

    def find_id(self, ids):
            return self.driver.find_element_by_id(ids)

    def find_xpath(self,xpath):
            return self.driver.find_element_by_xpath(xpath)
    
    def get_title(self):
         return self.driver.title
    
    def get_text(self, xpath):
         return self.driver.by_xpath(xpath).text
    
