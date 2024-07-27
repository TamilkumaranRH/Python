class student:
    def __init__(self,name ,rank ,point):
        self.name=name
        self.rank=rank
        self.point=point
    def gettername(self):
        print(self.name,self.point)
    def settername(self,name,point):
        self.name=name
        self.point=point
st1=student("arun",2,"15")
st1.settername("harish","20")
st1.gettername()
