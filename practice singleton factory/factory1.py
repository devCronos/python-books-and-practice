baseClass = type("baseClass",(object), {})

@classmethod
def check1(self,mystr):
    return mystr == "ham"

@classmethod
def check2(self,mystr):
    return mystr == "sandwich"


c1 = type("c1",(),{"x":1,"check":"check1"})
c2 = type("c2",(),{"x":30,"check":"check2"})

#def myFactory(myBool):
def myFactory(mystr):
   # return c1() if myBool else c2()
    for cls in baseClass.__subclasses__():
        if cls.check(mystr):
            return cls()


#m = myFactory(True)
#v = myFactory(False)
m = myFactory("ham",)
v = myFactory("sandwich")


print(m.x,v.x)