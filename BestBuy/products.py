class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product details.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity}, Price: ${self.price})"

    def get_quantity(self):
        """get current quantity of products"""
        return self.quantity

    def set_quantity(self, quantity):
        """set the quantity for the product"""
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """check if product is active"""
        return self.active

    def activate(self):
        """activating the product"""
        self.active = True

    def deactivate(self):
        """deactivating the product"""
        self.active = False

    def show(self):
        """product presentation name, price and quantity"""
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity):
        """purchase quantity of the product"""
        if quantity > self.quantity:
            raise Exception("Not enough quantity available.")

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


try:
    product = Product("Laptop", 1200, 5)
    print(product)
except ValueError as e:
    print(f"Error: {e}")
