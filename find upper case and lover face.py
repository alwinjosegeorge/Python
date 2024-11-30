def string():
  str="The quick Brow Fox"
  uppercount=0
  lowercount=0
  for i in str:
    if i.isupper():
         uppercount+=1
    elif i.islower():
            lowercount+=1
  print(uppercount)
  print(lowercount)
string()