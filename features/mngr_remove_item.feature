# Story 10
Feature: Delete an item from menu
    # Normal flow
    Scenario: The manager succesfully deletes an item from the menu
        Given that I am logged in
        When I select the task manager
        And I select to delete a menu item
        Then the menu item is removed