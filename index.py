class Breakfast:
    def __init__(self, food, drink):
        self.food = food
        self.drink = drink

    def getBF(self):
        return f'For breakfast, I had {self.food} and {self.drink}'


class Lunch:
    def __init__(self, salad, soup, drink):
        self.salad = salad
        self.soup = soup
        self.drink = drink


class Dinner:
    def __init__(self, salad, soup, entree, dessert):
        self.salad = salad
        self.soup = soup
        self.entree = entree
        self.dessert = dessert


mondayBreakfast = Breakfast('sardine', 'lipton tea')

print(mondayBreakfast.getBF())
