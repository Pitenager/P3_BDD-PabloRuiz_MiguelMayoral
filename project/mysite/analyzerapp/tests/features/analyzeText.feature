Feature: Analyze
    
    Background:
        Given the textarea not empty
        
    Scenario: Analyze a text
        When I write "chamber token chamber" in the textarea and press the "analyze" button
        
        Then The form should be submited, analyzing the text introduced
        
        And I shoud see the results:
        """
        ('chamber',2)
        ('token',1)
        """