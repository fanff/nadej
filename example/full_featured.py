# -*- coding: utf-8 -*-


import nadej
import loremipsum

def txt(i):
    return u"".join((_[2] for _ in loremipsum.generate_sentences(i)))


def img(x,y,topic=''):
    src= "http://lorempixel.com"
    url = "%s/%s/%s/%s"%(src,x,y,topic)

    
    import urllib2
    r = urllib2.urlopen(url)
    txt = r.read()

    import base64
    return base64.b64encode(txt)
    
n=nadej.nadej.ClientAPI()


n.title("Full Featured Example")
n.logo(img(400,400))
n.lead(txt(4))
n.summary("")


n.h1("Some basic features")

n.text(txt(4))


n.h2("h2 title")

n.text(txt(4))

n.h3("Some test results ")

n.test_s(txt(2))
n.test_s(txt(2))
n.test_f(txt(2))
n.test_f(txt(2))
n.test_s(txt(2))

n.h3("Rst formated text")

n.rst(txt(4))

n.split("vsplit",2)
n.rst("this is *italic* and this is **bold** and **both**")
n.rst(txt(4))
n.then()
n.rst("""
* this is list
* of some items 

""")
n.rst("""

#. this is list
#. of some items 

""")

n.split("end")


n.h3("image ")

n.png(img(800,300,))

n.h4("Rst formated text")
n.rst(txt(4))
n.h4("Rst formated text")
n.rst(txt(4))

n.h3("json ")

n.json([1,2,4])

import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(100, 5),
        columns=['adfq', 'bqvq', 'cfdqs', 'dfdsq', 'e'])

n.plot(df)




n.collect("html_bs:save in lol.html")
