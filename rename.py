import os

# for i in range(1,101):
#     os.rename(f"data/day{i}",f"data/Tutorial{i}")
folders=os.listdir("data")
print(folders)
for folder in folders:
    print(folder)


