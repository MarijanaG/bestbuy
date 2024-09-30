import products
from store import Store

def create_default_inventory():
    # stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    return product_list


def start(store: Store):
    while True:
        print("Welcome to our store")
        print("1.List all products in store")
        print("2.Show total amount in store")
        print("3.Make an order")
        print("4.Quit")

        user_choice = input("Please enter your choice: ")

        if user_choice == "1":
            products = store.get_all_products()
            if products:
                print("Available products ")
                for product in products:
                    print(product)
            else:
                print("No active products available")
        elif user_choice == "2":
            total_amount = store.get_total_quantity()
            print(f"Total amount of quantity is {total_amount}")
        elif user_choice == "3":
            shopping_list = []
            while True:
                product_name = input("Please enter the product name, or write 'done' to finish ")
                if product_name.lower() == "done":
                    break
                product = next((p for p in store.products if p.name.lower() == product_name.lower()), None)

                if product:
                    quantity = int(input("Enter quantity: "))
                    shopping_list.append((product, quantity))
                else:
                    print(f"Product not found in store ")

        elif user_choice == "4":
            print("Thanks for using application store ")
            break
        else:
            print("invalid choice ")


if __name__ == "__main__":
    store = Store()
    default_inventory = create_default_inventory()

    # Add products to the store
    for product in default_inventory:
        store.add_product(product)

    # Start the menu
    start(store)