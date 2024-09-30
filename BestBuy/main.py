import products
from store import Store

bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = products.Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

store = Store()

for product in product_list:
    store.add_product(product)

active_products = store.get_all_products()

products_store = store.get_all_products()
print(store.get_total_quantity())
print(store.order([(products_store[0], 1), (products_store[1], 2)]))
