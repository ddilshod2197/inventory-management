class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

class Do'kon:
    def __init__(self, nom, mahsulotlar):
        self.nom = nom
        self.mahsulotlar = mahsulotlar

class GroceryList:
    def __init__(self, mahsulotlar):
        self.mahsulotlar = mahsulotlar

    def hisoblash(self, do'konlar):
        umumiy_narx = 0
        for do'kon in do'konlar:
            for mahsulot in do'kon.mahsulotlar:
                if mahsulot in self.mahsulotlar:
                    umumiy_narx += mahsulot.narx
        return umumiy_narx

# Misol ma'lumotlar
mahsulotlar = [Mahsulot("Suv", 100), Mahsulot("Non", 200), Mahsulot("Milk", 300)]
do'konlar = [
    Do'kon("Do'kon 1", [Mahsulot("Suv", 90), Mahsulot("Non", 180), Mahsulot("Milk", 280)]),
    Do'kon("Do'kon 2", [Mahsulot("Suv", 110), Mahsulot("Non", 220), Mahsulot("Milk", 320)])
]

grocery_list = GroceryList(mahsulotlar)
print(grocery_list.hisoblash(do'konlar))
