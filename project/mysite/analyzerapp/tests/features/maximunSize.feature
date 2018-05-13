Feature: Text size control

    Scenario: Check the number of characters in textarea
        When I write in the textarea more than 100 characters
        Then I should see only the first 100