inventory=[
    ("laptop",5,1200.00), 
    ("Headphone",15,150.00),
    ("Mouse",50,150.00),
    ("Keyboard",20,150.00),
    ("Monitor",10,3000.00)
]
highest_stock_value=0
item_with_highest_stock_value=None
for item in inventory:
    item_name, quantity, unit_price=item
    stock_value=quantity * unit_price
    print(f"Item Name;{item_name},the stock value is : {stock_value}")
    if stock_value > highest_stock_value:
        highest_stock_value = stock_value
        item_with_highest_stock_value = item_name
print(f"Highest stock value is:{highest_stock_value}")
print(f"item with highest stock value is:{item_with_highest_stock_value}")
