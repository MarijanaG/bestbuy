class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def __str__(self):
        return f"{self.name} (Quantity: {self.quantity}, Price: ${self.price})"

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f'Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}'

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough quantity available")

        self.quantity -= quantity
        return self.price * quantity


try:
    product = Product("Laptop", 1200, 5)
    print(product)
except ValueError as e:
    print(f"Error: {e}")
