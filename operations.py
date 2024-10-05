from mimetypes import guess_type

a=10
b=5
#add two numbers
sum=a+b
#division
div=a/b
print("Sum:",sum ,",Divsion:",div)
#compare
gt=a>b
equality=a==b
print("Is a greater than b?:",gt)

print("Are a and b equal?:", equality)
#logical operators
AND= a>b and a!=b
OR= a>b or a==b
print("Logical AND:", AND)
print("Logical OR:" , OR)