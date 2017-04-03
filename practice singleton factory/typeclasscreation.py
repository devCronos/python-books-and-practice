class printHam(object):
    print("Ham")

TypeClass = type("TypeClass", (), {"prtinHam":printHam})

m=printHam()
t=TypeClass()

print(t)