def myfun(n):
    return lambda a:a*n
mydoubler = myfun(2)
mytriplet = myfun(3)
print(mydoubler(11))
print(mytriplet(12))
