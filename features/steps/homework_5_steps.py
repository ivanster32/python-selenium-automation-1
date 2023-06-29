from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, when, then

Product_Page= (By.CSS_SELECTOR, "#variation_color_name img")

Color_selection= (By.CSS_SELECTOR, 'span.selection')

@given('Open Amazon product page')
def open_amazon_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B08JQQLYQG/?th=1')


@then('Verify user can click through all colors')
def verify_user_can_click_through_all_orders(context):

Colors = Context.Driver.Find_elements(*Color_selection)

   for color in colors[:3]:
       color.click()
       current_color = context.driver_find_element(*Color_selection).text
       actual_colors +=[current_color]

    assert expected_colors == actual_colors, \
      f'Expected colors {expected_colors} did match actaul {actaul_colors}





    expected_colors = ['Black, Blue over Dye, Dark Blue Vintage, Dark Indigo, Dark Wash, Indigo Wash, Light Blue Vintage, Light Wash, Medium Blue Vintage, Medium Wash, Rinsed, Vintage Wash, light wash, Washed Black, Bright white, Dark Khaki Brown,m Light Khaki Brown, Olive, Washed Grey, Sage Green ']
    actual_results = ['Black, Blue Over Dye, Dark Blue Vintage, Dark Indigo, Dark Wash, Indigo Wash, Light Blue Vintage, Light Wash, Medium Blue Vintage, Medium Wash, Rinsed, Vintage Wash, light wash, Washed Black, Bright white, Dark Khaki Brown,m Light Khaki Brown, Olive, Washed Grey, Sage Green' ]
