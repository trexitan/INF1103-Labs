def get_valid_input():
        stock = input("Enter stock quantity: ")

        if stock == "quit":
            return"quit"
        
        elif not stock.isdigit():
            print("Error! Input must be a integer")
            return None
        
        return int(stock)

def process_delivery(current_total, new_value):
    current_total += new_value
    return current_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_units, failed_attempts):
    print("Total Units Processed:", total_units)
    print("Number of Failed Entries:", failed_attempts)

inventory_count = 0
failed_count = 0

while True:
    stock = get_valid_input()

    if stock == "quit":
        break
    if stock is None:
        failed_count += 1
        continue

    inventory_count = process_delivery(inventory_count, stock)

    tax = calculate_tax(stock)
    print("Tax Amount:", tax)

    if inventory_count > 500:
        print("Overstock Alert!")
        break

generate_report(inventory_count, failed_count)









