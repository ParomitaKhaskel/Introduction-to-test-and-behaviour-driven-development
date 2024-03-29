@delete_product
Feature: Product Management

  As a user
  In order to remove a product from the system
  I want to be able to delete a product

  Scenario: Deleting a Product
    Given I am on the homepage
    When I type in a Name that exists in the Background data and press the Search button
    Then I should see the message "Success" returned
    And I check that a field has an expected value
    When I copy the Id field, clear the form, paste the Id field and press the Delete button
    Then I should see the message "Product has been Deleted!"
    And I press the Clear button followed by the Search button
    Then I should not see the product in the results
    And I close the browser
