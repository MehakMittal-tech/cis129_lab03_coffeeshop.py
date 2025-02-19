# Coffee Shop Simulator

# Define prices
COFFEE_PRICE = 5
MUFFIN_PRICE = 4
TEA_PRICE = 3
CAKE_PRICE = 6

# Ask user for input
num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_teas = int(input("Number of teas bought? "))
num_cakes = int(input("Number of cakes bought? "))

# Calculate subtotal
subtotal = (num_coffees * COFFEE_PRICE) + (num_muffins * MUFFIN_PRICE) + (num_teas * TEA_PRICE) + (num_cakes * CAKE_PRICE)

# Calculate tax
tax = subtotal * 0.06

# Calculate total
total = subtotal + tax

# Display receipt
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${COFFEE_PRICE} each: ${num_coffees * COFFEE_PRICE:.2f}")
print(f"{num_muffins} Muffins at ${MUFFIN_PRICE} each: ${num_muffins * MUFFIN_PRICE:.2f}")
print(f"{num_teas} Teas at ${TEA_PRICE} each: ${num_teas * TEA_PRICE:.2f}")
print(f"{num_cakes} Cakes at ${CAKE_PRICE} each: ${num_cakes * CAKE_PRICE:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")

# Thank the user
print("Thank you for shopping at My Coffee and Muffin Shop!")