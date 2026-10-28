# Get customer information
customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")

# Get order information
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

# Calculate total
total_price = price * quantity

# Display summary
print("\n--- ORDER SUMMARY ---")
print(f"Customer: {customer_name.strip()}")
print(f"Product: {product_name.strip()}")
print(f"Quantity: {quantity}")
print(f"Total Amount: ₹{total_price:.2f}")