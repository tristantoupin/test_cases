# Story 12
Feature: Update item from the menu
    # Normal flow
    Scenario Outline: The manager successfully updates the name of an item to the menu
        Given that I am logged in
        When I select the task <task>
        Then the landing page of that task is open
        
    Examples: Tasks
     | task |
     | manager |
     | staff |
     | customer |