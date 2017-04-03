baseClass = type("baseClass",(), {})

c1 = type("c1",(),{"x":1})
c2 = type("c2",(),{"x":30})

def myFactory(myBool):
    return c1() if myBool else c2()

m = myFactory(True)
v = myFactory(False)

print m.x,v.x