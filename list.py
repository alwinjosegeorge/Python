my_list1=[]
my_list2=[]
my_list1_size = int(input("Enter size for the first list: "))
print("Enter the element of list1: ")
for i in range(my_list1_size):
    my_list1.append(int(input()))
my_list2_size = int(input("Enter size for the second list: "))
print("Enter the elements of list2: ")
for i in range(my_list2_size):
    my_list2.append(int(input()))
print(my_list1,my_list2)
combined_list=my_list1+my_list2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i % 2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("Even number in my list:", even_list)
print(odd_list)
even_list.sort()
odd_list.sort()