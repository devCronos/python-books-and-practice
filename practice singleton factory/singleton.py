class mySingleton(object):
    _instance = None
    def __new__(self):
        if not self._instance:
            self._instance=super(mySingleton,self).__new__(self)
            self.y=10
        return self._instance


x = mySingleton()
print(x.y)
x.y = 20

z= mySingleton()
print(z.y)