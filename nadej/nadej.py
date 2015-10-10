

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



    return u"""<html>%s %s</html>"""%(
            headText,
            bodyText
            )


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
    return u"<img></img>"

HTMLFORMAT_DIC = {
        "h1":htmlFormat_h1,
        "h2":htmlFormat_h2,
        "title":htmlFormat_title,
        "img":htmlFormat_img,

        }

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

    def collect(self,outpipe=""):
        """
        """

        if outpipe == "":
            ret = self.dataList
            self.dataList=[]
            return ret

        elif outpipe == "html":
            ret = self.dataList
            self.dataList=[]
            return htmlFormater(ret)

    def png(self,data):
        """
        """
        dic = {"type":"img",
               "form":"png",
               "data":data}
        self.dataList.append(dic)

