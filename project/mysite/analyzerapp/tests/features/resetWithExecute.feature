Feature: Reset textearea with execute button

    Scenario: Textarea with some text in it
        When I write in the textarea 
        And I click the execute button
        Then The textarea looks empty
        
        
        
    