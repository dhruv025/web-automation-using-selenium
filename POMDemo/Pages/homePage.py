class HomePage():

    def __init__(self,driver):

        self.driver = driver
        self.welcome_button_id = 'welcome'
        self.logout_button_linkTtext = 'Logout'

    def click_welcome(self):

        self.driver.find_element_by_id(self.welcome_button_id).click()

    def click_logout(self):
        
        self.driver.find_element_by_link_text(self.logout_button_linkTtext).click()