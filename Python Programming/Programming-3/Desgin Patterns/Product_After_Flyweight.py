class product_Meta_data :
    def __init__ (self, description, image, seller) :
        self.description = description
        self.image = image
        self.seller = seller
    def display (self) :
        print (f"وصف المنتج: {self.description} - صورة المنتج: {self.image} - بائع المنتج: {self.seller}")
class Product :
    _product_data = {}
    @classmethod
    def get_product_data (cls, description, image, seller) :
        key  = (description, image, seller)
        if key not in cls._product_data :
            cls._product_data[key] = product_Meta_data (description, image, seller)
        return cls._product_data[key]
class Product_Flyweight :
    def __init__ (self , name , price  , description , image , seller) :
        self.name = name
        self.price = price
        self.product_data = Product.get_product_data (description, image, seller)
    def display (self) :
        print (f"عرض المنتج: {self.name} - السعر: {self.price}")
        self.product_data.display ()
products = []
for i in range (1000) :
    products.append (Product_Flyweight (
        name = "iPhone 13",
        price = 999,
        description = "أحدث هاتف من آبل",
        image = "iphone13.jpg",
        seller = "Apple Store"
    ))
print (f"عدد المنتجات: {len (products)}")
