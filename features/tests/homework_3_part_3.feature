# Created by ivansantana at 6/15/23
Feature: Amazon shopping cart test

  Scenario: user can search for amazon Cart
    Given open main page
    When click on cart icon
    Then Verify your Amazon cart is empty
