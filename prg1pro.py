# student marks processing

student=[]
while True:
  print("1 for add student")
  print("2 for display")
  print("3 for exit")
  ch=int(input("enter your choice"))
  if ch==1:
     name=input("enter student name")
     marks=[]
     for x in range(3):
      m=float(input("enter 3 subject marks"))
      marks.append(m)
     total=sum(marks)
     per=total/3
     if(per>=60):
       div="II div"
     elif(per>=45 and per<60):
       div="III div"
     elif(per>=80):
       div="I div"
     else:
       div="fail"
     data={"name":name,
          "marks":marks,
          "total":total,
          "per":per,
          "div":div
          }
     student.append(data)
     print("record added")
  elif(ch==2): 
    if(len(student)==0):
      print("no record found")
    else:
      for x in student:
        print("name- ",x["name"])
        print("total marks- ",x["total"])
        print("per- ",x["per"]) 
        print("div- ",x["div"])

  elif(ch==3):
    break
  else:
    print("Invalid choice")
 
     


