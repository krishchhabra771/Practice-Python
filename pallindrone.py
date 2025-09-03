num=int(input("Enter the number"))
original =num
rev=0
while num>0 :
    n=len(str(num))
    digit=num%10
    rev=rev+digit*(10**(n-1))
    num=num//10
if(original==rev) :
    print("Pallindrome") 
else:
    print("Not an pallindrome")
