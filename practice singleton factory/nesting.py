def addOne(myFunc):
    def addOneInside(*args,**kwargs):
        return myFunc(*args,**kwargs)+1
    return addOneInside()
@addOne
def oldFunc(x=213):
    return x


print(oldFunc)