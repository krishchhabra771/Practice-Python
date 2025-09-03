num=int(input("enter the number"))
if(num==0 or num==1) :
    print("It is not an prime number")

elif(num>1):
    for i in range(2,num):
        if((num%i)==0):
            print("It is not an prime number")
            break
    else:
        print("It is an prime number")
else:
    print("it is not an prime number")    