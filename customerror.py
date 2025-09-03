# a=(input("enter the number b/w 5 and 9 :"))
# if a=='Quit':
#     print("thankyou")
# elif int(a)<5 or int(a)>9:
#     raise ValueError("value should be between 5 and 9")
# print("ty")

a= input("Enter the value between 5 and 9 : ")

if(a == "quite"):
    print("Thank You")
elif(int(a)<5 or int(a)>9):
    raise ValueError("The given item is invalid")
print("Thank You\nHave a Great Day")

