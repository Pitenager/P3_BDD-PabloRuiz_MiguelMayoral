Feature: Reset
    
    Scenario: Reset the textarea
        When I write text in the textarea

        Then I click the reset button

        And I should see the textarea empty