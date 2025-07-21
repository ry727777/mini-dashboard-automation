Feature: Add user functionality

  Scenario: Add User Page
    Given the user is on the "Add User Page"
    When the user enters "Rahul" as username, "12234" as order, and "1200" as revenue
    And click on Submit button
    Then user should see the alert "User created!"
