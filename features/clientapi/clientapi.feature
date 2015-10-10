Feature: Nadej provides a client API that
    accepts many kind of data such as title, heading, images and more.
    It provides a collect method that can output 
    a report file given options.


    Scenario: Nadej can manipulate Title
        Given I load the client API
        Given I call title with parameter "Title"
        Then a call to .collect returns a python list
        Then the list size is 1
        Then the list contains a "title" Element

    Scenario: Nadej can stay quiet
        Given I load the client API
        Then a call to .collect returns a python list
        Then the list size is 0

    Scenario: Nadej can manipulate Png Images
        Given I load the client API
        Given I call png with parameter "Title"
        Then a call to .collect returns a python list
        Then the list size is 1
        Then the list contains an "img" Element

    
