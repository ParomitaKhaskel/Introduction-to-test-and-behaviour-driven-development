from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    context.driver.get("http://example.com")  # Replace this with the URL of your homepage

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//button[text()='{button_text}']"))
    )
    button.click()

@then('I should see "{expected_text}"')
def step_impl(context, expected_text):
    result = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]"))
    )
    assert result.text == expected_text

@then('I should be redirected to "{url}"')
def step_impl(context, url):
    assert context.driver.current_url == url

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
