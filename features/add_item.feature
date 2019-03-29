# Story 9
Feature: Add item to the menu

	# Normal flow
	Scenario Outline: The manager successfully adds an item to the menu
		Given that I am logged in as a manager
		When I enter the price of an item <price>
		And I enter the name of an item <name>
		And I enter the description of an item <description>
		And I enter the inventory of an item <inventory>
		And I enter the tag of an item <tag>
		And submits the item
		Then the item with name <name> persists

	Examples: Price, names, descriptions, inventory quantities and tags
	 | price |  name | description | inventory | tag |
	 | 789 | jWVCTBfXrdzA | lCRsxXDHXHda | 123 | Appetizer |
	 | 678 | OnpVCMQFChcP | exwnNSCtzboF | 234 | Desert |
	 | 567 | NzlNTwYLuVAv | XcEsHzsBtGEC | 345 | Drink |
	 | 456 | bajAQrLKlnRy | bajAQrLKlnRy | 456 | Main Course |
	 | 345 | vUorAWQiVJrW | UcPyoxPaZuIr | 567 | Soup |
	 | 234 | cIKrSnAzqkSc | nyygyGUXbRNU | 678 | Spicy |
	 | 123 | PVJxbIrsjwkK | dYOGxSdrHqDW | 789 | Vegetarian |