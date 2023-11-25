# Create 2 dictionaries one containing grocery items and their prices and another containing grocery items and quantity purchased by using the values from these two, compute the total bill.
groceryItems={
    "Biscuit":50,
    "Banana":40,
    "Bread":49,
    "Butter":20
}
grocery_Quantity={
    "Biscuit":2,
    "Banana":1,
    "Bread":2,
    "Butter":1
}

totalBill=0

for item,price in groceryItems.items():
    quantity=grocery_Quantity.get(item,0)
    totalBill+=price*quantity
print("Total Bill = Rs",totalBill)