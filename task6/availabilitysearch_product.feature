@search_by_availability
Feature: Product Management

  As a user
  In order to find products based on availability
  I want to be able to search for products based on availability status

  Scenario: Searching a Product based on Availability
    Given I am on the homepage
    When I set the Available dropdown to True and press the Search button
    Then I should see the message "Success"
    And I check that available items from the Background data are in the results
    And the unavailable items are not in the results
    And I close the browser
