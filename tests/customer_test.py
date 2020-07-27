import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class cust_add(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_add_cust(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/customer/3/edit/")
       #fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)
       elem = driver.find_element_by_id("id_cust_number")
       elem.send_keys("12056 ")
       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Katherine McClusky ")
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("katherinemc@gmail.com")
       elem = driver.find_element_by_id("id_address")
       elem.send_keys("6782 Miles Street")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Ames")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("IA")
       elem = driver.find_element_by_id("id_zipcode")
       elem.send_keys("50010")
       elem = driver.find_element_by_id("id_cell_phone")
       elem.send_keys("515-554-3499")
       elem.send_keys(Keys.RETURN)

       time.sleep(100)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()