@list_all_products
Feature: Product Management

  As a user
  In order to view all available products
  I want to be able to list all products

  Scenario: Listing All Products
    Given I am on the homepage
    When I press the Clear button to remove the previous entries made
    And I press the Search button
    Then I should see the message "Success" returned
    And all the products such as "Hat", "Shoes", "Big Mac", and "Sheets" are seen in the results
    And I close the browser
