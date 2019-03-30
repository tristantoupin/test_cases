# Story 10
Feature: Update quantity of menu item
    # Normal flow
    Scenario: The manager succesfully updates the quantity of a menu item
        Given that I am logged in
        When I select the task manager
        And I select to update a menu item
        And I submit a valid new quantity
        Then the menu item quantity is changed