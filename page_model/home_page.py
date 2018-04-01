from locators.home_page import HomePageLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        
    @property
    def url(self):
        return 'http://nahual.github.io/qc-celfar/?v=3'
    
    @property
    def title(self):
        return self.driver.find_element(*HomePageLocators.TITLE)
    
    @property
    def description(self):
        return self.driver.find_element(*HomePageLocators.DESCRIPTION)
    
    @property
    def input_box(self):
        return self.driver.find_element(*HomePageLocators.INPUT_)
    
    @property
    def submit(self):
        return self.driver.find_element(*HomePageLocators.BUTTON)
    
    @property
    def output_box(self):
        return self.driver.find_element(*HomePageLocators.OUTPUT_)