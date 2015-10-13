@metadej
Feature: Nadej transform it own test report to bootstrap html
    
    Scenario: Produce nadej report to html
        Given I use testResult folder
        Then The file "testSrc/nadej_behave_out.json" exists
        And I call "python example/behave_j2html.py testSrc/nadej_behave_out.json testResult/nadej_behave_out.html"
        Then The file "testResult/nadej_behave_out.html" exists

