#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""
first = float( input("Enter First Price: ")) 
second = float( input("Enter Second Price: ")) 
third = float( input("Enter Third Price: ")) 
fourth = float( input("Enter Fourth Price: ")) 
fifth = float( input("Enter Fifth Price: ")) 
subtotal = first+second+third+fourth+fifth
tax = subtotal*0.12
total = subtotal + tax
tax = round(tax, 2)
total = round(total, 2)
print(f"Your subtotal is ${subtotal} and your taxes total ${tax} for a total of ${total}")