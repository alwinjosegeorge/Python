def mobile():
    number=input("Enter the Moble number:")
    if len(number)==10 and number[0] in ("7","8","9"):
        print("Number is valid:",number)
    else:
        print("The number is not valid:")
mobile()