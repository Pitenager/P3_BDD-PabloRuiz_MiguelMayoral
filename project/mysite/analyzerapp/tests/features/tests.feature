Feature: All the application

    Scenario: Analyze a text
        When I write chamber token chamber in the textarea
        
        Then I click the execute button
        
        And I should see the results:
    
    Scenario: Textarea empty
        When The textarea is empty
        And I click the execute button
        Then There is no result
        
    Scenario: Check the number of characters in textarea
        When I write in the textarea more than 100 characters
        Then I should see only the first 100
        
    Scenario: Reset the textarea
        When I write text in the textarea
        Then I click the reset button
        And I should see the textarea empty
        
    Scenario: Textarea with some text in it
        When I write in the textarea 
        And I click the execute button
        Then The textarea looks empty
        
    Scenario: Reset with no text
        When I have the textarea empty
        And I click the reset button
        Then The textarea continues empty