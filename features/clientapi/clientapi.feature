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

    
    Scenario: Nadej produce html reports with simple elements
        such as h1, h2, titles. html produced can be or not written 
        on disk via the collect method as being raw or embbeded in 
        html fields.
        Given I load the client API
        Given I call title with parameter "Title string"
        Given I call h1 with parameter "Firt part"
        Given I call h2 with parameter "below some image"
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

    Scenario Outline: Nadej produce html reports with simple elements
        such as h1, h2, titles. html produced can be or not written 
        on disk via the collect method as being raw or embbeded in 
        html fields.
        Given I load the client API
        Given I call title with parameter "Title string"
        Given I call h1 with parameter "Firt part"
        Given I call h2 with parameter "below some image"
        Given I call text with text parameter 
        """
        below some image
        """

        Given I call png with text parameter 
        """
        iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
        AAAOnAAADnUBiCgbeAAAABxJREFUCJlj/P///38GJMDEwMDAwNDIiCaAJAgA084FBkimv4oAAAAA
        SUVORK5CYII=
        """
        Given I call json with text parameter 
        """
        {"lfsk":"mfldsq"}
        """
        Given I call h2 with parameter "end doc ?"
        Given I call collect with parameter "<collectpipe>"
        Then the collect result is a unicode string
        Then the html result contains an "img" Element
        Then the html result contains 2 "h2" Elements
        Then the html result contains an "h1" Element
        Then the html result contains an "p" Element


        Examples: Embbeded html 
            | collectpipe                    | 
            | html                           | 
            | html:save in lol2.html         | 
        
        Examples: Inline html 
            | collectpipe                    | 
            | htmlinline                     | 
            | htmlinline:save in lol.html   | 
            

