class FoodItem:
    def __init__(self, foodId, foodName, price):
        self.foodId = foodId
        self.foodName = foodName
        self.price = price
        self.availability = False
    def updateFoodItem(self, price):
        self.price = price
    def switchAvailability(self):
        self.availability = not self.availability