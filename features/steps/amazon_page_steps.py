from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ORDER_BUTTON = (By.CSS_SELECTOR, 'a[href="/gp/css/order-history?ref_=nav_orders_first"]')
SIGNIN_HEADER = (By.CSS_SELECTOR, 'h1.a-spacing-small')
# EMAIL_FIELD = (By.CSS_SELECTOR, '#ap_email')



@given('Open Amazon Page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on Orders')
def click_orders(context):
    context.driver.find_element(*ORDER_BUTTON).click()


@then('Verify Sign In Page is opened')
def verify_signin_opens(context):
    actual_text = context.driver.find_element(*SIGNIN_HEADER)
    assert expected_result == actual_result, f'error! expected {expected_result}bot got a '
