'''
Python progress to sum of dight of number
'''
number=int(input("Enter a number"))
sum=0
while(number>0):
    r=number%10
    number=number//10
    sum=sum+r
print(sum)