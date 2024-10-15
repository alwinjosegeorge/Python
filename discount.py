'''
Python progress to check calculates the final mount after applying the discount
'''
amount=int(input("Enter the purchars amount"))
if amount>500:
    discount=amount*20/100
    final_amount=amount-discount
    print(final_amount)
elif amount>200 and amount<=500:
    discount=amount*10/100
    final_amount=amount-discount
    print(final_amount)
else:
    print("No discount applied")