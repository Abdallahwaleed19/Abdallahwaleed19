class Product:
    def __init__(self, name, price, description, image, seller, category):
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.seller = seller
        self.category = category
    
    def display(self):
        print(f"عرض المنتج: {self.name} - السعر: {self.price}")

products = []
for i in range(1000):
    products.append(Product(
        name="iPhone 13",
        price=999,
        description="أحدث هاتف من آبل",
        image="iphone13.jpg",
        seller="Apple Store",
        category="Smartphones"
    ))
print(f"عدد المنتجات: {len(products)}")