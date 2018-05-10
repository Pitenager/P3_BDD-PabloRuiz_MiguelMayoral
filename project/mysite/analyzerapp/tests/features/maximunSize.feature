Feature: Text size control

    Scenario: Check the number of characters in textarea
    
        When I write in the textarea
        
        Then I should not be able to use more than 100 characters
        
        And The textarea does not allow me to write anymore