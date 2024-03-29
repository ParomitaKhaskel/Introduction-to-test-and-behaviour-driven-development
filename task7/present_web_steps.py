from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    context.driver.get("http://example.com")  # Replace this with the URL of your homepage

@then('I should see the message "{expected_message}"')
def step_impl(context, expected_message):
    result = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_message}')]"))
    )
    assert result.text == expected_message

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
