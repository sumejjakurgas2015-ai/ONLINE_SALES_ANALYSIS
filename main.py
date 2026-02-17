from product import Product
from product_manager import ProductManager

# Kreiramo ProductManager
manager = ProductManager()

# Dodajemo proizvode
p1 = Product("Laptop PRO", 2000, 2)
p2 = Product("Mouse", 25, 20)
p3 = Product("Keyboard", 80, 10)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz svih proizvoda
print("=== Lista proizvoda ===")
manager.show_products()

# Ukupna vrijednost inventara
p1 = Product("Laptop", 1500, 3)

print("\nRemoving Mouse...")
manager.remove_product("Mouse")

print("\nLista nakon uklanjanja:")
manager.show_products()
from cart import Cart
cart = Cart()

# dodaj 3 proizvoda iz manager liste
cart.add_to_cart(p1)
cart.add_to_cart(p2)
cart.add_to_cart(p3)

cart.show_cart()
print("\nUkupno za naplatu:", cart.total_cart_value())
