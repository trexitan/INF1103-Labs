inventory_count = 0
failed_count = 0

while True:
    stock = input("Enter stock quantity: ")

    if stock == "quit":
        break
        
    elif not stock.isdigit():
        print("Error! Input must be a integer")
        failed_count += 1
        continue
    stock = int(stock)
    inventory_count += stock

    if inventory_count > 500:
        print("Overstock Alert!")
        break
print("Total Units Processed:", inventory_count)
print("Number of Failed Entries:",failed_count)
