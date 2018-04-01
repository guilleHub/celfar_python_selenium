from selenium.webdriver.common.by import By

class HomePageLocators():
    
    TITLE = By.TAG_NAME, 'h1'
    DESCRIPTION = By.ID, 'description'
    INPUT_ = By.ID, 'input'
    OUTPUT_ = By.ID, 'output'
    BUTTON = By.CLASS_NAME, 'button'
    LINK_CELCIUS = By.XPATH, ".//*[@id='description']/a[1]"
    LINK_FAHRENHEIT = By.XPATH, ".//*[@id='description']/a[2]"