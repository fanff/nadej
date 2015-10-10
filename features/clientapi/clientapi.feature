
Feature: Nadej provides a client API
    Scenario: Nadej define a client API
        Given I load the client API
        And this base method list
            | name | Description |
            | h1   | Heading 1   |
            | h2   | Heading 2   |
            | collect   | Flush result   |

        Given we call each method on the api
        Then it does not raise Exception
        Then a call to .collect returns a python list


