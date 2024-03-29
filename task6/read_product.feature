@read_product
Feature: Product Management

  As a user
  In order to view product details
  I want to be able to read a product

  Scenario: Reading a Product
    Given I am on the homepage
    When I click the "View Product" button
    Then I should see the details of the product
    And I close the browser
