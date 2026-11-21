try:
 x=open("myfile1.txt","r")
 s=x.read()
 mprint ("fiule content-",s)
except FileNotFoundError:
    print("file not found")