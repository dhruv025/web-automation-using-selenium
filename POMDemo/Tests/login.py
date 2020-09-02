from selenium import webdriver
import time
import unittest
import sys
sys.path.append('.')
from POMDemo.Pages.loginPage import LoginPage
from POMDemo.Pages.homePage import HomePage
import HtmlTestRunner

class loginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='/home/dhruv/chromedriver')

        cls.driver.implicitly_wait(10)
        
        cls.driver.maximize_window()

    def test_login_valid(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

        login = LoginPage(self.driver)

        login.enter_username('Admin')
        login.enter_password('admin12345')
        login.click_login()

        home = HomePage(self.driver)

        home.click_welcome()
        home.click_logout()
            
        time.sleep(2)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

        cls.driver.quit()

        print("Test Completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/dhruv/SeleniumProject/Reports'))