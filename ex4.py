a=int(input("enter the number 1 for Code 2 for Decode:"))
if a==1:
    b=input("Enter the word to code:")

    if len(b)>3:
       c='abc'+b[1:-1]+b[0]+'def'
       print(c)
    else:
       d=b[-1]+b[0]
elif a==2:
   e=input("Enter the word to decode:")

   if len(e)>9:
      f=e[-4]+e[3:-4]
      print(f)
   else:
      g=e[-4]+e[3]
      print(g)

else:
   print("Warning-Read the statement correctly")



