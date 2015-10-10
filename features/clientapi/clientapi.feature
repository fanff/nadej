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

    
    Scenario: Nadej produce html report with many kind of data 
        Given I load the client API
        Given I call title with parameter "Title string"
        Given I call h1 with parameter "h1 text"
        Given I call h2 with parameter "h2 text"
        Given I call png with text parameter 
            """
                iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
                AAAOnAAADnUBiCgbeAAAABxJREFUCJlj/P///38GJMDEwMDAwNDIiCaAJAgA084FBkimv4oAAAAA
                SUVORK5CYII=
            """

        Given I call collect with parameter "html"
        Then the collect result is a unicode string
        Then the html result contains an "img" Element
        Then the html result contains an "h2" Element
        Then the html result contains an "h1" Element
        Then the html result contains a "title" Element
    
    Scenario: Nadej produce html report with two images and  two h2
        Given I load the client API
        Given I call title with parameter "Two image"
        Given I call png with text parameter 
            """
                iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
                AAAOnAAADnUBiCgbeAAAABxJREFUCJlj/P///38GJMDEwMDAwNDIiCaAJAgA084FBkimv4oAAAAA
                SUVORK5CYII=
            """

        Given I call png with text parameter 
            """
                iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
                AAAOnAAADnUBiCgbeAAAABxJREFUCJlj/P///38GJMDEwMDAwNDIiCaAJAgA084FBkimv4oAAAAA
                SUVORK5CYII=
            """

        Given I call h2 with parameter "h2 first"
        Given I call h2 with parameter "h2 next"
        Given I call collect with parameter "html"
        Then the collect result is a unicode string
        Then the html result contains 2 "img" Elements
        Then the html result contains 2 "h2" Elements

