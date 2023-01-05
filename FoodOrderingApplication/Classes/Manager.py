from User import User
from Restaurant import Restaurant
from FoodItem import FoodItem

class Manager(User):
    def __init__(self, userId, name, phoneNumber):
        User.__init__(self, userId, name, phoneNumber)
        self.restaurant = None
    def addRestaurant(self, restaurant):
        if(self.restaurant == None):
            self.restaurant = restaurant
            return True
        else:
            return False
    def addFoodItem(self, foodId, foodName, price):
        if(self.restaurant == None):
            return False
        self.restaurant.foodItems.append(FoodItem(foodId, foodName, price))
        return True
    def removeRestaurant(self):
        self.restaurant = None
    def updateRestaurantStatus(self, status):
        self.restaurant.status = status
    #def updateRestaurantDetails(self):
