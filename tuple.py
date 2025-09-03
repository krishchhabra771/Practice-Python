tup=(1,2,3,4,5)
print(tup[2:5])
print(tup)

#tuple method
# there is no directly method to add or remove item we will convert it 
# into list first afterwards u can print in tuple

countries=("spain","india","England","Japan","russia","finland")
# temp=list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[1]="finland"
# countries=tuple(temp)
# print(countries)


print(countries.index("russia",2,5))