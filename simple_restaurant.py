print("WELCOME TO THE RESTAURANT!")
print("| ---------------||---------|")
print("| SANDWICHES     || COST    |")
print("| ---------------||---------|")
print("| chicken -------|| $5.25   |")
print("| beef ----------|| $6.25   |")
print("| tofu ----------|| $5.75   |")
print("| ---------------||---------|")
print("| BEVERAGES      || COST    |")
print("| ---------------||---------|")
print("| small ---------|| $1.00   |")
print("| medium --------|| $1.75   |")
print("| large ---------|| $2.25   |")
print("| ---------------||---------|")
print("| FRENCH FRIES   || COST    |")
print("| ---------------||---------|")
print("| small ---------|| $1.00   |")
print("| medium --------|| $1.50   |")
print("| large ---------|| $2.00   |")
print("| ---------------||---------|")
print("| KETCHUP        || $0.25   |")
print("| ---------------||---------|")


sandwich_prices = {'chicken': 5.25, 'beef': 6.25, 'tofu': 5.75}
beverage_prices = {'small': 1.00, 'medium': 1.75, 'large': 2.25}
fries_prices = {'small': 1.00, 'medium': 1.50, 'large': 2.00}
ketchup_price = 0.25

selected_sandwich = input("Select a sandwich (chicken, beef, tofu): ").lower()
while selected_sandwich not in sandwich_prices:
    selected_sandwich = input("Select a sandwich correctly (chicken, beef, tofu): ").lower()

 

total_cost = sandwich_prices[selected_sandwich]



want_beverage = input("Do you want a beverage? (yes/no): ").lower()
if want_beverage == 'yes':
    selected_size = input("Choose beverage size (small, medium, large): ").lower()
    while selected_size not in beverage_prices:
        selected_size = input("Choose beverage size correctly (small, medium, large): ").lower()
    total_cost += beverage_prices[selected_size]



print(f"Total cost so far: {total_cost:.2f}")



want_fries = input("Do you want fries? (yes/no): ").lower()
if want_fries == 'yes':
    selected_size = input("Choose fries size (small, medium, large): ").lower()
    while selected_size not in fries_prices:
        selected_size = input("Choose fries size correctly (small, medium, large): ").lower()
    fries_price = fries_prices[selected_size]

   

    if selected_size == 'small' and input("Mega-size your fries for $2.00? (yes/no): ").lower() == 'yes':
        fries_price = fries_prices['large']
        total_cost -= 1.00

    total_cost += fries_price



    print(f"Total cost so far: {total_cost:.2f}")



ketchup_packets = input("How many ketchup packets? (Enter a positive integer): ")

while not ketchup_packets.isdigit() or int(ketchup_packets) < 0:

    ketchup_packets = input("Invalid input. Please enter a positive integer for ketchup packets: ")



total_cost += int(ketchup_packets) * ketchup_price

print(f"Total cost so far: {total_cost:.2f}")



print(f"Your order:")

print(f"- {selected_sandwich} sandwich: {sandwich_prices[selected_sandwich]:.2f}")

if want_beverage == 'yes':

    print(f"- {selected_size} beverage: {beverage_prices[selected_size]:.2f}")

if want_fries == 'yes':

    print(f"- {selected_size} fries: {fries_price:.2f}")

print(f"- ketchup packets: {int(ketchup_packets) * ketchup_price:.2f}")

print(f"Total cost: {total_cost:.2f}")

restart = input("Would you like to edit your order (yes)(no)? ")
if restart == "yes":
        re = input("Would you like to edit you sandwich, beverage, or fries? ")
        if re == "sandwich":
                selected_sandwich = input("Select a sandwich (chicken, beef, tofu): ").lower()
                while selected_sandwich not in sandwich_prices:
                    selected_sandwich = input("Select a sandwich correctly (chicken, beef, tofu): ").lower()
                total_cost = sandwich_prices[selected_sandwich]
            
            

                
