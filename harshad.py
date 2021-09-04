a=int(input("enter the number:"))
i=a
sum=0
while i>0:
    sum=sum+(i%10)
    i=i//10
if a%sum==0:
    print("harshad")
else:
    print("no")