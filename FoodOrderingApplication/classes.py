class FoodItem:
    def __init__(self, food_id, restaurant_id, name, description, price, availability=False):
        self.food_id = food_id
        self.restaurant_id = restaurant_id
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
    def updateFoodItem(self, price):
        self.price = price
    def switchAvailability(self):
        self.availability = not self.availability

class User:
    def __init__(self, email, name, contact, address = None, area_id = None):
        self.email = email
        self.name = name
        self.contact = contact
        self.area_id = area_id
        self.address = address

class Manager(User):
    def __init__(self, email, name, contact, area_id = None, restaurant = None):
        User.__init__(self, email, name, contact, area_id)
        self.restaurant = restaurant
    def add_restaurant(self, restaurant):
        if(self.restaurant == None):
            self.restaurant = restaurant
            return True
        else:
            return False
    def removeRestaurant(self):
        self.restaurant = None
    #def updateRestaurantDetails(self):

class Restaurant:
    def __init__(self, id, manager_email, name, open_time, close_time, address, area_id, phone, flag = False):
        self.name = name
        self.id = id
        self.manager_email = manager_email
        self.area_id = area_id
        self.close_time = close_time
        self.open_time = open_time
        self.phone = phone
        self.address = address
        self.foodItems = []
        self.orders = []
        self.flag = flag

    def toggleFlag(self):
        if self.flag == False:
            self.flag = True
        else:
            self.flag = False

    def addFoodItem(self, foodItem):
        self.foodItems.append(foodItem)

    #def getStatus(self):
        #return self.status
    #def displayFoodItems(self):

class cart_item:
    def __init__(self, item_id, user_id, food_id):
        self.item_id = item_id
        self.user_id = user_id
        self.food_id = food_id

class Order:
    def __init__(self, order_id, food_items, customer_email, status, delivery_person_email, city):
        self.order_id = order_id
        self.food_items = food_items
        self.customer_email = customer_email
        self.status = status
        self.delivery_person_email = delivery_person_email
        self.city = city