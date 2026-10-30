from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def find(self, product_name: str) -> Product | None:
        return next((product for product in self.products if product_name == product.name), None)

    def add(self, product: Product):
        self.products.append(product)

    def remove(self, product_name: str):
        product = self.find(product_name)

        if product is not None:
            self.products.remove(product)

    def __repr__(self):
        return "\n".join([f"{product.name}: {product.quantity}" for product in self.products])
