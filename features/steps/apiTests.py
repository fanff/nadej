from behave import *
import nadej
import json



@given(u'this base method list')
def step_impl(context):
    """

    * Mapping method names to actual method
    * Verify each method name is present in the dic

    """
    context.methodMap = {}
    context.methodMap["h1"] = nadej.h1
    context.methodMap["h2"] = nadej.h2

    for row in context.table:
        context.methodMap["h1"] = nadej.h1

@when(u'we call each method on the api')
def step_impl(context):
    for mname,meth in context.methodMap.items():
        meth()

@then(u'it does not raise Exception')
def step_impl(context):
    pass

@then(u'a call to .collect returns a python list')
def step_impl(context):
    res = nadej.collect()

    assert isinstance(res,list)


@given(u'I call {name} on the Nadej module')
def step_impl(context,name):
    if name == "h1":
        context.methodToCall = nadej.h1
    elif name == "h2":
        context.methodToCall = nadej.h2
    
@given(u'I use this parameter {parameter} on the method')
def step_impl(context,parameter):
    context.methodToCall(parameter)

@then(u'a call to .collect returns {resultDic}')
def step_impl(context,resultDic):
    resultDicPython = json.loads(resultDic)
    res = nadej.collect()
    assert resultDicPython == res



