from behave import *
from selenium import webdriver

from page_model.home_page import HomePage

use_step_matcher('re')

@given(u'I am on the home page')  # @UndefinedVariable
def step_impl(context):
    context.driver = webdriver.Chrome('e:/drivers/chromedriver.exe')
    page = HomePage(context.driver)
    context.driver.get(page.url)

