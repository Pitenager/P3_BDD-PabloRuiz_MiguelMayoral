Feature: Reset with no text

    Scenario: Reset with no text
        When I have the textarea empty
        And I click the reset button
        Then The textarea continues empty