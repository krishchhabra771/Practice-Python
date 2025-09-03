import time
# t=time.strftime('%H')
hour=int(time.strftime('%H'))
print (hour)
if(hour>0 and hour<12):
    print("good morning!!")
elif(hour>12 and hour<18):
    print("good evening!!")
else :
     print("good night!!")    