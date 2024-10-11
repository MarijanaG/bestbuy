from products import DigitalProduct, NonStockedProduct
class Store:

    def __init__(self):
        self.products = []

    def __str__(self):
        return f"Products in store: {[product.name for product in self.products]}"

    def add_product(self, product):
        #adding product in the list
        self.products.append(product)

    def remove_product(self, product):
        #remove product from the list when is not active anymore
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products:
            if isinstance(product, DigitalProduct) or isinstance(product, NonStockedProduct):
                # Skip products with unlimited or no stock
                continue
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        #get all active products in store
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        #making an order product and quantity
        total_price = 0.0

        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                try:
                    total_price += product.buy(quantity)
                except "Exception" as e:
                    print(f"Error buying product: {e}")
            else:
                print(f"Product {product.name} is not available or not active.")

        return total_price



