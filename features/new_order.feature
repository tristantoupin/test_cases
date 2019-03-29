# Story 2 and 5
Feature: Create an order
    # Normal flow
    Scenario: The customer successfully creates an order
        Given that I am logged in as a custumer and browsing a categorie of items
        When I select an item from the menu to add to my card
        And navigate to the cart
        And submit the order
        Then the staff receives a new oder