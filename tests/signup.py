import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class sign_up(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_signup(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/SignUp")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys("Angela")
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("Angela@gmail.com")
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("angela")
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("mathew")
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys("abcd$1234")
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys("abcd$1234")
       elem.send_keys(Keys.RETURN)

       assert "Logged In"
       time.sleep(50)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()