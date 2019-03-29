# Story 3 and 8
Feature: Request the bill
    # Normal flow
    Scenario: The customer successfully review and request the bill
        Given that I am logged in as a custumer
        When I navigate to the bill
        And submit a request to the staff to pay the bill
        And the staff receives a new bill request
        Then the staff clears the bill request

