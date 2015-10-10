Feature: Nadej provides a python api

    Scenario: Nadej define a python api for writing document elements
        Given I load the native API
        Given this base method list
            | name | Description |
            | title| Document Title |
            | h1   | Heading 1   |
            | h2   | Heading 2   |
            | collect   | Flush result   |

        Given we call each method on the api
        Then it does not raise Exception
        Then a call to .collect returns a python list

    Scenario Outline: Nadej define a python api that outputs standardised data dict
        Given I load the native API
        Given I call <name> on the Nadej module 
        Given I use this parameter <parameter> on the method 
        Then a call to .collect returns <result>

        Examples: Heading 1
            | name | parameter | result |
            | h1   | test!     | [{"type":"h1","text":"test!"}] |
            | h1   | lol       | [{"type":"h1","text":"lol"}]   |
            
        Examples: Heading 2
            | name | parameter | result |
            | h2   | test!     | [{"type":"h2","text":"test!"}] |

