import products
import promotions
from store import Store
from datetime import date


def create_default_inventory():
    """Stock of inventory with new product types"""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),  # Regular Product
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),  # Regular Product
        products.Product("Google Pixel 7", price=500, quantity=250),  # Regular Product
        products.DigitalProduct("E-Book", price=20),  # Digital Product (unlimited)
        products.PerishableProduct("Milk", price=5, quantity=50, expiration_date=date(2024, 10, 12)),
        products.NonStockedProduct("Windows License", price=125),  # Non-stocked Product
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)  # Limited Product
    ]

    second_half_price = promotions.SecondItemHalfPrice("Second Half price!")
    third_one_free = promotions.BuyTwoGetOneFree("Third One Free!")
    thirty_percent = promotions.PercentageDiscount("30% off!", percentage=30)

    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    return product_list


def start(store: Store):
    while True:
        print("Welcome to our store")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. List promotions")
        print("5. Quit")

        user_choice = input("Please enter your choice: ")

        if user_choice == "1":
            available_products = store.get_all_products()
            if available_products:
                print("Available products:")
                for available_product in available_products:
                    print(available_product.show())
            else:
                print("No active products available")

        elif user_choice == "2":
            total_amount = store.get_total_quantity()
            print(f"Total amount of quantity is {total_amount}")

        elif user_choice == "3":
            shopping_list = []
            while True:
                product_name = input("Please enter the product name, or write 'done' to finish: ")
                if product_name.lower() == "done":
                    break
                product = next((p for p in store.get_all_products() if p.name.lower() == product_name.lower()), None)

                if product:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity <= 0:
                            print("Quantity must be a positive integer.")
                            continue
                        if quantity > product.get_quantity():
                            print(f"Not enough {product.name} available. Current quantity: {product.get_quantity()}.")
                            continue
                        shopping_list.append((product, quantity))
                    except ValueError:
                        print("Please enter a valid integer for quantity.")
                else:
                    print(f"Product '{product_name}' not found in store.")

            for purchased_product, quantity in shopping_list:
                try:
                    total_cost = purchased_product.buy(quantity)
                    print(f"Purchased {quantity} of {purchased_product.name}. Total cost: ${total_cost}.")
                except Exception as e:
                    print(f"Error purchasing {quantity} of {purchased_product.name}: {e}")

        elif user_choice == "4":
            print("Available promotions:")
            for product in store.get_all_products():
                promotion_info = product.promotion.name if product.promotion else "No promotion"
                print(f"{product.name}: {promotion_info}")

        elif user_choice == "5":
            print("Thanks for using the application store.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    store = Store()
    default_inventory = create_default_inventory()

    # Add products to the store
    for product in default_inventory:
        store.add_product(product)

    # Start the menu
    start(store)
