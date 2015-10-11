@metadej
Feature: Nadej transform it own test report to bootstrap html
    
    Scenario: Produce nadej report to html
        Then The file "nadej_behave_out.json" exists
        And I call "python example/behave_j2html.py nadej_behave_out.json nadej_behave_out.html"
        Then The file "nadej_behave_out.html" exists

