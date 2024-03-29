@search_by_name
Feature: Product Management

  As a user
  In order to find products based on name
  I want to be able to search for products based on their name

  Scenario: Searching a Product based on Name
    Given I am on the homepage
    When I type in the name of the product and press the Search button
    Then I should see the message "Success"
    And I check that available items from the Background data are in the results
    And the unavailable items are not in the results
    And I close the browser
