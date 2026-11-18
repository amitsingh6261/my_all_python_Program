import calendar
print(calendar.month(2026,12))
print("====================")

import keyword
print(keyword.kwlist)
print("========================")


import time
x=time.time()
print("second-",x)
time.localtime(x)
print(time.localtime(x))
print("===gmtime===")
print(time.gmtime(x))
print("===c time===")
print(time.ctime(x))
print("===============")


x=time.strftime("%a")
print(x)
x=time.strftime("%A")
print(x)
x=time.strftime("%d")
print(x)
x=time.strftime("%D")
print(x)
x=time.strftime("%y")
print(x)
x=time.strftime("%b")
print(x)

x=time.strftime("%a-%d-%m-%y")
print(x)

x=time.strftime("%A-%d-%m-%y-%H-%M-%S-%p")
print(x)
print("==================")
x=time.strftime("%j")
print(x)