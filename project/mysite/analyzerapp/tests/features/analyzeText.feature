Feature: Analyze
        
    Scenario: Analyze a text
        When I write chamber token chamber in the textarea
        Then I click the execute button
        And I should see the results: