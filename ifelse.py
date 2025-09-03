# a=303300
# b=30333
# print("A") if a>b else print("=") if a==b else print("B")

# c=9 if a>b else 0
# print(c)

# Enumerate function
marks =[1,3,4,564,43,3,2,1]
for index ,mark in enumerate( marks,start=1):
    print(index,mark)
    if index==3:
        print("heyyyyy")