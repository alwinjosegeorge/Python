my_list=[22,12,65,96,12,18]
unique_list=[]
for number in my_list:
    if number not in  unique_list:
        unique_list.append(number)
print("The original list is:",my_list)
print(unique_list)