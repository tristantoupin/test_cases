# Story 6
Feature: Change status of an order
   # Normal flow
   Scenario Outline: The staff successfully changes the status of an order
       Given that I am logged in as a staff
       When I navigate the orders
       And the customer submits and order
       And changes the status of the order to <status>
       Then the status persists
   Examples:
    | status |
    | in progress |
    | served |
    | ready |