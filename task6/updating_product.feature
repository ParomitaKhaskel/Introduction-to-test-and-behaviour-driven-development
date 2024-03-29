@update_product
Feature: Product Management

  As a user
  In order to update product information
  I want to be able to edit a product

  Scenario: Updating a Product
    Given I am on the homepage
    When I type in a Name that exists in the Background data and press the Search button
    Then I should see the message "Success" returned
    And I check that a field has an expected value
    When I change one of the fields and press the Update button
    Then I should see the message "Success"
    And I copy the Id field, clear the form, paste the Id field and press the Retrieve button
    Then I should see the message "Success"
    And I check that the field I updated has the new value
    And I press the Clear button followed by the Search button
    Then I should see the changed field in the results
    And I close the browser
