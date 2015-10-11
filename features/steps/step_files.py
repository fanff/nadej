import os
import subprocess


@then(u'The file "{filename}" exists')
def step_impl(context,filename):
    assert os.path.exists(filename), u"file %s does not exists"%filename

@then(u'I call "python example/behave_j2html.py {fileIN} {fileOUT}"')
def step_impl(context,fileIN,fileOUT):
    
    callArray=["python","example/behave_j2html.py",
            fileIN,
            fileOUT
            ]
    res = subprocess.check_output(" ".join(callArray),shell=True)

