# Story 1
Feature: Browse item in the menu
   # Normal flow
   Scenario: The customer successfully browses the menu
       Given that I am logged in as a custumer
       When I select a category to browse
       And selects an item of the menu
       Then I see a description of the item

