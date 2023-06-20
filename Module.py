def create_shopping_cart():
    shopping_cart = {}

    while True:
        print("\n--- Shopping Cart ---")
        print("1. Add item")
        print("2. Delete item")
        print("3. View shopping cart")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            quantity = input("Enter the quantity: ")
            shopping_cart[item] = quantity
            print("Item '{}' added to the shopping cart.".format(item))
        elif choice == '2':
            item = input("Enter the item to delete: ")
            if item in shopping_cart:
                del shopping_cart[item]
                print("Item '{}' removed from the shopping cart.".format(item))
            else:
                print("Item '{}' not found in the shopping cart.".format(item))
        elif choice == '3':
            print("\nCurrent shopping cart:")
            if shopping_cart:
                for item, quantity in shopping_cart.items():
                    print("{} - {}".format(item, quantity))
            else:
                print("The shopping cart is empty.")
        elif choice == '4':
            print("\nFinal shopping cart:")
            if shopping_cart:
                for item, quantity in shopping_cart.items():
                    print("{} - {}".format(item, quantity))
            else:
                print("The shopping cart is empty.")
            break
        else:
            print("Invalid choice. Please try again.")

create_shopping_cart()



