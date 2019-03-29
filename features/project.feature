Feature: showing off behave

Scenario: Select Staff task
	Given we have logged in
	When we select staff task
	Then we verify we are on staff landing

Scenario: Select Customer task
	Given we have logged in
	When we select customer task
	Then we verify we are on customer landing

Scenario: Select Manager task
	Given we have logged in
	When we select manager task
	Then we verify we are on manager landing