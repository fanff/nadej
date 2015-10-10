Feature: Nadej produce html

    Scenario Outline: Produce html with multiple elements
        such as h1, h2, titles etc.. . Html can be written 
        on disk and be "raw" or "embbeded" in <html> fields.
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
            


