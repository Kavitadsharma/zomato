menu = [{
    'id': '1',
    'name': 'Margherita Pizza',
    'price': 12.99,
    'availability': 'yes'
},
{
    'id': '2',
    'name': 'Pasta Alfredo',
    'price': 9.99,
    'availability': 'yes'
},
 {
    'id': '3',
    'name': 'Garlic Bread',
    'price': 4.99,
    'availability': 'no'
}]
orders = []

def add_dish():
    dish_id = input("Enter the dish ID: ")
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Is the dish available? (yes/no): ")

    dish = {
        'id': dish_id,
        'name': dish_name,
        'price': price,
        'availability': availability
    }

    menu.append(dish)
    print("Dish added successfully.")

def remove_dish():
    dish_id = input("Enter the dish ID to remove: ")
    removed = False

    for dish in menu:
        if dish['id'] == dish_id:
            menu.remove(dish)
            removed = True
            break

    if removed:
        print("Dish removed successfully.")
    else:
        print("Dish not found.")

def update_availability():
    dish_id = input("Enter the dish ID to update availability: ")
    availability = input("Is the dish available? (yes/no): ")
    updated = False

    for dish in menu:
        if dish['id'] == dish_id:
            dish['availability'] = availability
            updated = True
            break

    if updated:
        print("Availability updated successfully.")
    else:
        print("Dish not found.")

def take_order():
    customer_name = input("Enter customer name: ")
    dish_ids = input("Enter dish IDs (separated by commas): ").split(",")
    order = {
        'customer_name': customer_name,
        'dish_ids': dish_ids,
        'status': 'received'
    }

    available_dishes = []
    unavailable_dishes = []

    for dish_id in dish_ids:
        dish_found = False

        for dish in menu:
            if dish['id'] == dish_id:
                if dish['availability'] == 'yes':
                    available_dishes.append(dish)
                    dish_found = True
                else:
                    unavailable_dishes.append(dish)
                    dish_found = True
                break

        if not dish_found:
            print(f"Dish with ID {dish_id} not found in the menu.")

    if len(unavailable_dishes) > 0:
        print("The following dishes are unavailable:")
        for dish in unavailable_dishes:
            print(f"- {dish['name']}")
    else:
        print("Order processed successfully.")
        order_id = len(orders) + 1
        order['order_id'] = order_id
        orders.append(order)

def update_order_status():
    order_id = int(input("Enter the order ID to update status: "))
    new_status = input("Enter the new status: ")
    updated = False

    for order in orders:
        if order['order_id'] == order_id:
            order['status'] = new_status
            updated = True
            break

    if updated:
        print("Order status updated successfully.")
    else:
        print("Order not found.")

def review_orders():
    if len(orders) == 0:
        print("No orders placed yet.")
    else:
        print("Order Review:")
        for order in orders:
            print(f"Order ID: {order['order_id']}")
            print(f"Customer Name: {order['customer_name']}")
            print("Dishes:")
            for dish_id in order['dish_ids']:
                dish = next((item for item in menu if item['id'] == dish_id), None)
                if dish:
                   


                    print(f"- {dish['name']}")
            print(f"Status: {order['status']}")
            print()

def exit_program():
    print("Exiting the program. Have a great day!")

# Main program flow
while True:
    print("Welcome to Zomato")
    print("1. Add a new dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update dish availability")
    print("4. Take a new order")
    print("5. Update order status")
    print("6. Review all orders")
    print("7. Show Menu")
    print("8. Exit")
    
    choice = input("Enter your choice (1-7): ")
    
    if choice == '1':
        add_dish()
    elif choice == '2':
        remove_dish()
    elif choice == '3':
        update_availability()
    elif choice == '4':
        take_order()
    elif choice == '5':
        update_order_status()
    elif choice == '6':
        review_orders()
    elif choice =="7":
        print(menu)
    elif choice == '8':
        exit_program()
        break
    else:
        print("Invalid choice. Please try again.")



