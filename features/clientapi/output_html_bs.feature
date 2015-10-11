Feature: Nadej produce bootstrap formated pages
    @work
    Scenario Outline: Produce html bootstraped 
        with multiple elements
        Given I load the client API
        Given I call title with parameter "Title string"
        Given I call h1 with parameter "Firt part"
        Given I call text with text parameter 
        """
        Showing some features
        """
        Given I call h2 with parameter "Drawing image"
        Given I call text with text parameter 
        """
        This image in embbed in the document
        """

        Given I call png with text parameter 
        """
        iVBORw0KGgoAAAANSUhEUgAAAAQAAAADCAYAAAC09K7GAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
        AAAOnAAADnUBiCgbeAAAABxJREFUCJlj/P///38GJMDEwMDAwNDIiCaAJAgA084FBkimv4oAAAAA
        SUVORK5CYII=
        """
        Given I call h2 with parameter "Some json"
        Given I call json with text parameter 
        """
        {"lfsk":"mfldsq"}
        """
        Given I call h2 with parameter "Example for table"
        Given I call text with text parameter 
        """
        After loading csv in pandas
        """
        Given I load a pandas frame from text csv in register df
        """
        a   , b   , c
        1   , 2   , 2
        2.5   , 3   , 2
        3   , 2   , 1
        3   , 2   , 1
        1   , 2   , 2
        2.5   , 3   , 2
        0  , 2   , 1
        1   , 2   , 2
        2.5   , 0   , 2
        1   , 2   , 2
        2.5   , 3   , 2
        3   , 2   , 1
        1   , 0   , 2
        2.5   , 3   , 2
        3   , 2   , 1
        1   , 2   , 2
        2.5   , 3   , 2
        3   , 2   , 1
        """
        Given I call table with register df
        Given I call h2 with parameter "as plot"
        Given I call plot with register df
        Given I call collect with parameter "<collectpipe>"
        Then the collect result is a unicode string
        Then the html result contains 2 "img" Elements

        Examples: Bootstrap html 
            | collectpipe                    | 
            | html_bs:save in lol2.html      | 
        
            

