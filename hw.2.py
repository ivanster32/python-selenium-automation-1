Part 1
1) [i.a-icon.a-icon-logo
2) input#continue.a-button-input
3) [span.a-expander-prompt]
4)[a#auth-fpp-link-bottom.a-link-normal]
5)[a#ap-other-signin-issues-link.a-link-normal]
6)[a#createAccountSubmit.a-button-text]
7)[a.a-link-normal, a#auth-fpp-link-bottom.a-link-normal,
8)[a.a-link-normal, a#auth-fpp-link-bottom.a-link-normal


part 2




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get ('https://www.amazon.com/')
driver.find_element(By.ID, 'https://www.amazon.com/gp/css/order-history?ie=UTF8&ref_=nav_orders_first' )


expected_result = 'sign in page than order history'
actual_result = 'sign in page and shows order history'


