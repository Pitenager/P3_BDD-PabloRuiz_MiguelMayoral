Feature: Click execute having no text in textarea

    Scenario: Textarea empty
        When The textarea is empty
        And I click the execute button
        Then There is no result
        
