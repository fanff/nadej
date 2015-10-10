



class InnerData(object):

    dataList = []


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

    def collect(self):
        """
        """
        ret = self.dataList
        self.dataList=[]
        return ret
        


innerData = InnerData()

h1=innerData.h1
h2=innerData.h2
collect=innerData.collect
