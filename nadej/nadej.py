
import os
from StringIO import StringIO

def htmlFormater(dataList):
    """


    """
    
    headArray=[]
    bodyArray=[]
    for elem in dataList:

        if elem["type"] == "title":
            res=htmlFormat_title(elem)

            headArray.append(res)
        else:

            res=HTMLFORMAT_DIC[elem["type"]](elem)
            bodyArray.append(res)

    headText = u"<head> %s  </head>"%(u" ".join(headArray))
    
    bodyText = u"<body>%s</body>"%(u" ".join(bodyArray),)



    return u"""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
%s 
%s
</html>"""%(
            headText,
            bodyText
            )

def htmlInlineFormater(dataList):
    """

    """
    bodyArray=[]
    for elem in dataList:
        if elem["type"] == "title":
            pass
        else:
            res=HTMLFORMAT_DIC[elem["type"]](elem)
            bodyArray.append(res)
    return u" ".join(bodyArray)

def htmlFormat_table(elem):
    """
    """
    import pandas as pd
    if elem["format"] == "pd.frame":
        return elem["data"].to_html()
    else:
        raise Exception("elem format not supported %s"%(elem["format"]))
def htmlFormat_title(elem):
    """
    """
    return u"<title>%s</title>"%elem["text"]
def htmlFormat_h1(elem):
    """
    """
    return u"<h1>%s</h1>"%elem["text"]
def htmlFormat_h2(elem):
    """
    """
    return u"<h2>%s</h2>"%elem["text"]
def htmlFormat_img(elem):
    """
    """

    if elem["format"] == "png":

        return u"""
    <img alt="Embedded Image" 
        src="data:image/png;base64,%s" />
"""%(elem["data"])

def htmlFormat_code(elem):
    """
    """
    return u"<pre>%s</pre>"%elem["text"]

def htmlFormat_p(elem):
    """
    """
    return u"<p>%s</p>"%elem["text"]

HTMLFORMAT_DIC = {
        "h1":htmlFormat_h1,
        "h2":htmlFormat_h2,
        "title":htmlFormat_title,
        "img":htmlFormat_img,
        "p":htmlFormat_p,
        "code":htmlFormat_code,
        "table":htmlFormat_table,

        }
def savein(data,dest):
    """

    save data in html
    """
    if os.path.isabs(dest) :
        return
    
    
    if dest.endswith(".html"):
        with open(dest,"w") as ou:
            ou.write(data)
    else:
        raise Exception ("Format not accepted")
class ClientAPI(object):

    def __init__(self):
        self.dataList=[]

    def title(self,text=""):
        """
        Clean up buffer
        """
        self.dataList=[]
        dic = {"type":"title",
                "text":text}
        self.dataList.append(dic)

    def h1(self,text=""):
        """
        """

        dic = {"type":"h1",
                "text":text}
        self.dataList.append(dic)
        

    def h2(self,text=""):
        """
        """
        dic = {"type":"h2",
                "text":text}
        self.dataList.append(dic)

    def json(self,text=""):
        dic = {"type":"code",
                "format":"json",
                "text":text}
        self.dataList.append(dic)

    def text(self,text=""):
        """
        """
        dic = {"type":"p",
                "text":text}
        self.dataList.append(dic)

    def table(self,data=""):
        """
        """
        import pandas as pd
        dic = {"type":"table",
                "format":"pd.frame",
                "data":data
                }
        self.dataList.append(dic)
    def png(self,data):
        """
        data should be base64
        """
        dic = {"type":"img",
               "format":"png",
               "data":data}
        self.dataList.append(dic)


    def plot(self,data=""):
        """
        """
        import pandas as pd

        if isinstance(data,pd.DataFrame):
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            plt.plot(data)
            
            plt.legend(data.columns)

            bufferIMG = StringIO()
            plt.savefig(bufferIMG)
            from base64 import b64encode,b64decode

            buffer64 = b64encode(bufferIMG.getvalue())

            self.png(buffer64)

        else:
            raise Exception("not supported yet")

    def collect(self,outpipe=""):
        """
        """
        ret = self.dataList
        self.dataList=[]

        if outpipe == "":
            return ret
        
        pipe = outpipe.split(":")
        for step in pipe:
            if step == "html":
                ret= htmlFormater(ret)
            elif step == "htmlinline":
                ret= htmlInlineFormater(ret)
            elif step.startswith("save in"):
                dest = step.lstrip("save in ")
                savein(ret,dest)

            else:
                raise Exception("pipe error at step %s"%step)

        return ret

