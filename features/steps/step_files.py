import os
import subprocess

@given(u'I use {foldername} folder')
def step_impl(context,foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername)

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

@given(u'I call "python example/full_featured.py {fileOUT}"')
def step_impl(context,fileOUT):
    
    callArray=["python","example/full_featured.py",
            fileOUT
            ]
    res = subprocess.check_output(" ".join(callArray),shell=True)

