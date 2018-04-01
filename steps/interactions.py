from behave import *
from page_model.home_page import HomePage

use_step_matcher('re')

@when('I enter "(.*)" in the input box')
def step_impl(context, content):
    page = HomePage(context.driver)
    page.input_box.send_keys(content)
    
@step('I click the submit button')
def step_impl(context):
    page = HomePage(context.driver)
    page.submit.click()