Feature: Query the staff

Scenario: The customer successfully queries the staff
    Given that I am logged in as a custumer
    When I request the staff for help
    And the staff receives a new help request
    Then the staff clears the request

