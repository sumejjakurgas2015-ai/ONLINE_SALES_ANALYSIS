from product import Product
from product_manager import ProductManager

# Kreiramo ProductManager
manager = ProductManager()

# Dodajemo proizvode
p1 = Product("Laptop", 1200, 5)
p2 = Product("Mouse", 25, 20)
p3 = Product("Keyboard", 80, 10)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# Prikaz svih proizvoda
print("=== Lista proizvoda ===")
manager.show_products()

# Ukupna vrijednost inventara
print("\nUkupna vrijednost inventara:")
print(manager.total_inventory_value())
print("\nRemoving Mouse...")
manager.remove_product("Mouse")

print("\nLista nakon uklanjanja:")
manager.show_products()
