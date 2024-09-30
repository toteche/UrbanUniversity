class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            products = file.readlines()
            file.close
            return ''.join(product.strip() + '\n' for product in products)
        except FileNotFoundError:
            return "Файл с продуктами не найден"

    def add(self, *products):
        existing_products = self.get_existing_products()

        for product in products:
            if product.name in existing_products:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close

    def get_existing_products(self):
        try:
            file = open(self.__file_name, 'r')
            existing_products = set()
            for line in file:
                existing_products.add(line.split(',')[0].strip())
            file.close()
            return existing_products
        except FileNotFoundError:
            return set()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
