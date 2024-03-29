from behave import given, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()  # Initialize the Chrome WebDriver
    context.driver.get("http://example.com")  # Replace this with the URL of your homepage

@then('I should not see "{unexpected_text}"')
def step_impl(context, unexpected_text):
    try:
        WebDriverWait(context.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, f"//*[contains(text(), '{unexpected_text}')]"))
        )
    except TimeoutError:
        pass  # If element with unexpected text is not found, it means the test passed
    else:
        assert False, f"Found unexpected text: {unexpected_text}"

@then('I close the browser')
def step_impl(context):
    context.driver.quit()
