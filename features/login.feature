# Story 12
Feature: Slect device task
    # Normal flow
    Scenario Outline: The manager successfully selects the task of the device
        Given that I am logged in
        When I select the task <task>
        Then the landing page of that task is open
        
    Examples: Tasks
     | task |
     | manager |
     | staff |
     | customer |