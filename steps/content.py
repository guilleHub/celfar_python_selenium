from behave import *

from page_model.home_page import HomePage

use_step_matcher('re')

@then('There is a title shown on the page')
def step_impl(context):
    page = HomePage(context.driver)
    assert page.title.is_displayed()

@step('The title is "(.*)"')
def step_impl(context, content):
    page = HomePage(context.driver)
    assert page.title.text == content
    
@then('There is a description shown on the page')
def step_impl(context):
    page = HomePage(context.driver)
    assert page.description.is_displayed()
    
@step('The description says "(.*)"')
def step_impl(context, content): 
    page = HomePage(context.driver)
    assert page.description.text == content
        
@then('The output is "(.*)"')
def step_impl(context, content):
    page = HomePage(context.driver)
    assert page.output_box.text == content