a=int(input("enter no of students"))
b=[]
for i in range(a):
    temp={}
    temp["name"]=input("enter name of student")
    temp["marks"]=int(input("enter marks"))
    temp["percentage"]=float(input("enter percentage"))
    b.append(temp)
for i in range(0,a):
    for j in range(0,a-i-1):
        if b[j]["name"]>b[j+1]["name"]:
            b[j],b[j+1]=b[j+1],b[j]
for i in range(a):
    print(b[i])
for i in range(a):
 if b[i]['marks'] > 39:
     print(b[i]['name'], " PASS ")
 else:
     print(b[i]['name'], " FAIL ")
