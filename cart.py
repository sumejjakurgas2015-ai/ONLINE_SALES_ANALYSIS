from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def add_to_cart(self, product: Product):
        self.cart_items.append(product)

    def total_cart_value(self):
        return sum(p.price * p.quantity for p in self.cart_items)

    def show_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
            return
        print("=== Cart items ===")
        for p in self.cart_items:
            p.display_info()
