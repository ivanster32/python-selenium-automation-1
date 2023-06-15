from selenium.webdriver.common.by import By
from behave import given, when, then

CART_ICON = (By.CSS_SELECTOR, 'div#nav-cart-count-container')
CART_TEXT = (By.XPATH, '//div[@class="a-row sc-your-amazon-cart-is-empty"]/h2')

@given ('open main page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com')


@when ('click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@then ('Verify your Amazon cart is empty')
def verify_your_amazon_page_is_open(context):
      actual_text = context.driver.find_element(*CART_TEXT).text
      expected_text = "Your Amazon Cart is empty"
      assert expected_text == actual_text, f"Expected text is {expected_text} but got {actual_text}"


