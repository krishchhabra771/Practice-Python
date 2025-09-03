# a=input("enter the number")
# print(f"Multiplication of {a} is:")
# try:
#     for i in range(1,11):
#         print(f"{(a)} X {i}={int(a)*i}")
# except :      
#     print("Invalid input")
# print("some imp lines of code")   
# print("end of code")     
def func():
    try:
        num=int(input("enter the number"))
        a=[7,3]
        print(a[num])
        return 1
    except ValueError :
        print("please enter an integer")
        return 0
    except IndexError:
        print("index error!") 
        return 0

    finally:
        print("I am always executable")
x=func()
print(x)

