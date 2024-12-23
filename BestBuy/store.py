from products import DigitalProduct, NonStockedProduct
class Store:
    """Represents a store that holds products, allowing adding, removing, and managing products.
        It supports operations such as calculating total quantities, fetching active products, and processing orders.
        """
    def __init__(self):
        """Initializes the store with an empty list of products."""
        self.products = []

    def __str__(self):
        """Returns a string representation of the store, listing the names of all products available in the store."""
        return f"Products in store: {[product.name for product in self.products]}"

    def add_product(self, product):
        """Adds a product to the store's inventory."""
        #adding product in the list
        self.products.append(product)

    def remove_product(self, product):
        """Removes a product from the store's inventory, typically when the product is not active anymore."""
        self.products.remove(product)

    def get_total_quantity(self):
        """Calculates and returns the total quantity of all products in the store that have a limited stock."""
        total_quantity = 0
        for product in self.products:
            if isinstance(product, DigitalProduct) or isinstance(product, NonStockedProduct):
                # Skip products with unlimited or no stock
                continue
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Returns a list of all active products in the store."""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """Processes an order by calculating the total price for the products and quantities in the shopping list."""
        total_price = 0.0

        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                try:
                    total_price += product.buy(quantity)
                except Exception as e:
                    print(f"Error buying product: {e}")
            else:
                print(f"Product {product.name} is not available or not active.")

        return total_price



