from datetime import datetime


class Product:
    """Represents a product with a name, price, quantity, and optional promotion.
        Allows managing product details such as quantity, activation, and promotion.
        """
    def __init__(self, name, price, quantity):
        """Initializes a new product with the provided name, price, and quantity."""
        if not name or (price is None or price < 0) or (quantity is not None and quantity < 0):
            raise ValueError("Invalid product details.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None

    def __str__(self):
        """Returns a string representation of the product, including its name, quantity, and price."""
        return f"{self.name} (Quantity: {self.quantity}, Price: ${self.price})"

    def set_promotion(self, promotion):
        """Set a promotion for the product."""
        self.promotion = promotion

    def show(self):
        """Product presentation name, price, quantity, and promotion."""
        promotion_info = f" (Promotion: {self.promotion.name})" if self.promotion else " (No promotion)"
        return f'Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}{promotion_info}'

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

    def buy(self, quantity):
        """Buys a specified quantity of the product, deducting from the stock and calculating the total cost."""
        if self.quantity >= quantity:
            self.quantity -= quantity  # Deduct the purchased amount
            total_cost = self.price * quantity

            # Apply promotion if available
            if self.promotion:
                total_cost, free_items = self.promotion.apply_promotion(self, quantity)
                if free_items > 0:
                    print(f"You get {free_items} free item(s) with this promotion!")
            return total_cost
        else:
            raise ValueError(f"Not enough {self.name} available or product is not in stock.")


try:
    product = Product("Laptop", 1200, 5)
    print(product)
except ValueError as e:
    print(f"Error: {e}")


class NonStockedProduct(Product):
    """Represents a product that is not stocked (e.g., digital products or back-order items)."""
    def __init__(self, name, price):
        """Initializes a non-stocked product with the given name and price."""
        super().__init__(name, price, 0)

    def show(self):
        """Returns a description of the non-stocked product, including its name, price, and promotion status.
"""
        return f"{self.name} (Price: ${self.price}, Non-stocked) - {self.promotion.name if self.promotion else 'No promotion'}"


class DigitalProduct(Product):
    """Represents a digital product that has no limits on quantity (i.e., an infinite stock).
"""
    def __init__(self, name, price):
        """Initializes a digital product with the provided name and price."""
        super().__init__(name, price, None)

    def show(self):
        """Returns a description of the digital product, emphasizing its unlimited quantity."""
        return f"Digital Product - Name: {self.name}, Price: {self.price} (Unlimited Quantity)"


class LimitedProduct(Product):
    """Represents a product with limited stock, enforcing a maximum quantity that can be purchased.
    """
    def __init__(self, name, price, quantity, maximum):
        """Initializes a limited product with the provided name, price, quantity, and purchase limit."""
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        """Returns a description of the limited product, including its promotion status and purchase limit."""
        promo_info = f"Promotion: {self.promotion.name}" if self.promotion else "No promotion"
        return f"{self.name} (Price: ${self.price}, Quantity: {self.quantity}, Max: {self.maximum}) - {promo_info}"

    def buy(self, quantity):
        """Buys a specified quantity of the limited product, enforcing the purchase limit."""
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} of {self.name}.")
        return super().buy(quantity)


class PerishableProduct(Product):
    """Represents a perishable product with an expiration date."""
    def __init__(self, name, price, quantity, expiration_date):
        """Initializes a perishable product with the provided name, price, quantity, and expiration date."""
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date

    def is_expired(self):
        """Check if the product is expired"""
        today = datetime.today().date()
        return today > self.expiration_date

    def show(self):
        """Show product with special characteristics for perishable products"""
        expired_status = "Expired" if self.is_expired() else "Fresh"
        return (f"Perishable Product - Name: {self.name}, Price: {self.price}, "
                f"Quantity: {self.quantity}, Expiration Date: {self.expiration_date} ({expired_status})")
