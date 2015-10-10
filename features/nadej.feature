Feature: Nadej write doc for you

    Scenario: Nadej define a python api for writing document elements
        Given this base method list
            | name | Description |
            | h1   | Heading 1   |
            | h2   | Heading 2   |

        When we call each method on the api
        Then it does not raise Exception
        Then a call to .collect returns a python list

    Scenario Outline: Nadej define a python api that outputs standardised data dict
        Given I call <name> on the Nadej module 
        Given I use this parameter <parameter> on the method 
        Then a call to .collect returns <resultDic>

        Examples: Heading 1
            | name | parameter | resultDic |
            | h1   | test!     | [{"type":"h1","text":"test!"}] |
            | h1   | lol       | [{"type":"h1","text":"lol"}]   |
            
        Examples: Heading 2
            | name | parameter | resultDic |
            | h2   | test!     | [{"type":"h2","text":"test!"}] |
            

