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


n.title("Summary example")
n.logo(img(400,400))
n.lead(txt(4))
n.summary("")


n.h1("1. "+txt(1))
n.text(txt(4))

n.h2("1.1. "+txt(1))
n.text(txt(4))

n.h3("1.1.1 "+txt(1))
n.text(txt(4))

n.h3("1.1.2 "+txt(1))
n.text(txt(4))

n.h3("1.1.3 "+txt(1))
n.text(txt(4))

n.h2("1.2. "+txt(1))
n.text(txt(4))

n.h3("1.2.1 "+txt(1))
n.text(txt(4))

n.h3("1.2.2 "+txt(1))
n.text(txt(4))

n.h1("2. "+txt(1))


n.h3("2.1.1 "+txt(1))
n.text(txt(4))

n.h4("2.1.1.1 "+txt(1))
n.text(txt(4))

n.h4("2.1.1.2 "+txt(1))
n.text(txt(4))

n.h3("2.1.2 "+txt(1))
n.text(txt(4))

n.h1("3. "+txt(1))

n.h3("3.1.1 "+txt(1))
n.text(txt(4))

n.h4("3.1.1.1 "+txt(1))
n.text(txt(4))

n.h4("3.1.1.2 "+txt(1))
n.text(txt(4))



n.collect("html_bs:save in /home/fanf/Bin/lol.html")
