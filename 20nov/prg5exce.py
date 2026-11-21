try:
  n=5
  m=int(input("enter the value"))
  res=n/m
  print(res)
except ZeroDivisionError:
  print("no must be > zero")
else:
   print("result",res)
finally:
  print("this is execute always")
  