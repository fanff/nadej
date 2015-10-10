from behave import *
import nadej
import json



@given(u'I load the client API')
def step_impl(context):
    
    newClient = nadej.nadej.ClientAPI()
    context.nadej = newClient
    context.nadej_TestRegister = {}
    assert len(context.nadej.dataList) == 0

@given(u'I load the native API')
def step_impl(context):
    context.nadej = nadej

@given(u'this base method list')
def step_impl(context):
    """
    * Mapping method names to actual method
    * Verify each method name is present in the dic
    """
    context.methodMap = {}
    context.methodMap["h1"] = context.nadej.h1
    context.methodMap["h2"] = context.nadej.h2
    context.methodMap["collect"] = context.nadej.collect
    context.methodMap["title"] = context.nadej.title

    context.tablecontent = []
    for row in context.table:
        row["name"] in context.methodMap
        context.tablecontent.append(row["name"])

@given(u'we call each method on the api')
def step_impl(context):
    for name in context.tablecontent:
         context.methodMap[name]()

@then(u'it does not raise Exception')
def step_impl(context):
    pass


@then(u'the collect result is a unicode string')
def step_impl(context):
    assert isinstance(context.nadej_collected,unicode),"Should be unicode"

@then(u'a call to .collect returns a python list')
def step_impl(context):
    res = context.nadej.collect()
    context.nadej_collected = res
    assert isinstance(res,list)

@then(u'the list size is {count}')
def step_impl(context,count):

    print(context.nadej_collected)
    c = int(count)
    assert len(context.nadej_collected) == c

@given(u'I call {name} on the Nadej module')
def step_impl(context,name):
    if name == "h1":
        context.methodToCall = context.nadej.h1
    elif name == "h2":
        context.methodToCall = context.nadej.h2
    elif name == "title":
        context.methodToCall = context.nadej.title
    elif name == "png":
        context.methodToCall = context.nadej.png
    elif name == "collect":
        context.methodToCall = context.nadej.collect
    else:
        assert False,"No such method %s"%name
@given(u'I use this parameter {parameter} on the method')
def step_impl(context,parameter):
    context.methodToCall(parameter)

@then(u'a call to .collect returns {resultDic}')
def step_impl(context,resultDic):
    resultDicPython = json.loads(resultDic)
    res = context.nadej.collect()
    context.nadej_collected = res
    assert resultDicPython == res

@given(u'I call {method} with parameter "{someText}"')
def step_impl(context,method,someText):

    if method == "collect":

        res = context.nadej.collect(someText) 
        context.nadej_collected=res
    else:
        context.execute_steps("""
            given I call %s on the Nadej module
            given I use this parameter %s on the method
        """%(method,someText))


@then(u'the list contains {num} "{elemid}" Element')
def step_impl(context,num,elemid):
    
    if num in ("a","an"):
        print("list contains",context.nadej_collected)
        for elem in context.nadej_collected:
            if elem["type"] in elemid :
                return True

        # coming here means failure
        assert False

    else:
        raise NotImplementedError(u'STEP: Then the list contains a title Element')


@given(u'I call {method} with text parameter')
def step_impl(context,method):
    if method == "png":
        context.nadej.png(context.text)
    elif method == "text":
        context.nadej.text(context.text)
    elif method == "json":
        context.nadej.json(context.text)
    else:
        assert False ,"Method does not exists"

@given(u'I call {apimethod} with register {register}')
def step_impl(context,apimethod,register):
    method = apimethod

    if method == "png":
        context.nadej.png(context.nadej_TestRegister[register])
    elif method == "text":
        context.nadej.text(context.nadej_TestRegister[register])
    elif method == "json":
        context.nadej.json(context.nadej_TestRegister[register])
    elif method == "table":
        context.nadej.table(context.nadej_TestRegister[register])
    elif method == "plot":
        context.nadej.plot(context.nadej_TestRegister[register])
    else:
        assert False ,"Method does not exists"



@then(u'the html result contains {nocare} "{domelem}" Element')
def step_impl(context,domelem,nocare):
    from bs4 import BeautifulSoup
    print("src",context.nadej_collected)
    soup = BeautifulSoup(context.nadej_collected, 'html.parser')
    
    res = soup.find_all(domelem)

    print("lol",soup.prettify())
    assert len(res) == 1

@then(u'the html result contains {some} "{domelem}" Elements')
def step_impl(context,some,domelem):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(context.nadej_collected, 'html.parser')
    
    res = soup.find_all(domelem)
    assert len(res) == int(some)


@given(u'I load a pandas frame from text csv in register {reg}')
def step_impl(context,reg):
    import pandas as pd
    from StringIO import StringIO 


    s = StringIO(context.text)
    df = pd.read_csv(s)
    context.nadej_TestRegister[reg] = df

