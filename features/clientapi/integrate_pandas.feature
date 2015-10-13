Feature: Nadej can output pandas dataframe as plot or tables 
    
    Scenario Outline: Simple pandas frame handling
        Given I load the client API
        Given I use testResult folder
        Given I call h1 with parameter "Showing some pandas integration"
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
        Given I call h2 with parameter "as table"
        Given I call table with register df
        Given I call h2 with parameter "as plot"
        Given I call plot with register df
        Given I call collect with parameter "<collectpipe>"
        
        Examples: Some outputs 
            | collectpipe                    | 
            | html                           | 
            | html:save in testResult/lol2.html         |



