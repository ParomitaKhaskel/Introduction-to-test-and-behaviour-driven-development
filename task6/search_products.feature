@search_by_category
Feature: Product Management

  As a user
  In order to find products within a specific category
  I want to be able to search for products based on category

  Scenario: Searching a Product based on Category
    Given I am on the homepage
    When I clear the page
    And I select the "Food" category and press the Search button
    Then I should see the message "Success"
    And I check that "Big Mac" is in the results
    And other foods from the Background data are not in the results
    And I close the browser
