num=int(input("Enter the number"))
original=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num//10
if(sum==original):
    print("armstrong number") 
else:
    print("Not an armstrong number")    


