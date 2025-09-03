questions=[
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],
    ["Who is the most legally hacker in the world ?","Kevin Mitnick ","Adrian lamo ","Kelvin Poulsen","Michael Calcae","None",1],


]


    


Level=[1000,2000,3000,5000,7000,9000,11000,15000,21000,51000,10000000,30000000,50000000,60000000,70000000]
i=0
money=0
for i in range(0,len(questions)):
    Question=questions[i]
    print(f"Question for Rs.{Level[i]} \n{Question[0]}")
    print(f"1.{Question[1]}       2.{Question[2]}")
    print(f"1.{Question[3]}       2.{Question[4]}")
    reply=int(input("Enter the number (1-4) "))
    if reply==Question[-1]:
        print(f"Correct answer ,You won Rs. {Level[i]}\n")
        if i==3:
            money=5000

        elif i==8 :
            money=21000

        elif i==13:
            money=60000000
    else:
        print("Wrong answer") 
        break 
print(f"Your take home money is{money}")


