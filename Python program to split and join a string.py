'''
Python program to get the student details
Author; Alwin Jose George
Date:08-10-2024
version: 1.0
'''

first_name=input("Enter your first name")
last_name=input("Enter your last name")
full_name= first_name +" " +last_name
length=len(first_name)
extracted_last_name=full_name[length+1:]
print(full_name)
print(length)
print(extracted_last_name)
