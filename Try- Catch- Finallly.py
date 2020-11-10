import math
num=int(input("Enter Value"))
try:
    result=math.factorial(num)
    print(result)
except:
    print("Negative value has no factorial")
finally:
    print("bye")
