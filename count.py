def calculate_discount(price, discount_percent):
    if discount_percent>=20:
        discount_price=price-(price*(discount_percent/100))
        return discount_price
    else:
        return price

original_price=float(input("Enter the original price of the item: "))
discount_percent=float(input("Enter the discount percentage: "))

Final_price=calculate_discount(original_price, discount_percent)
print(f"Final price after applying the discount:", {Final_price})

    