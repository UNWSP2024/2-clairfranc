# Program 3, Claire Francis, Jan 21, 2025

def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    # then displays the subtotal of the sale,
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.

    item1 = float(input("insert cost of item1:"))
    item2 = float(input("insert cost of item2:"))
    item3 = float(input("insert cost of item3:"))
    item4 = float(input("insert cost of item4:"))
    item5 = float(input("insert cost of item5:"))

    subtotal_of_sale = (item1 + item2 + item3 + item4 + item5)
    print("$",format(subtotal_of_sale, '.2f'))
    sales_tax = ((float(subtotal_of_sale)) * 0.07)
    print("$",format(sales_tax, '.2f'))
    print("$",format(subtotal_of_sale + sales_tax, '.2f'))

calculate_total_purchase()
