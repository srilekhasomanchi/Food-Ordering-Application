class Restaurant:
    def __init__(self, name, id, manager, area, address, phoneNumber):
        self.name = name
        self.id = id
        self.manager = manager
        self.area = area
        self.address = address
        self.phoneNumber = phoneNumber
        self.foodItems = []
        self.orders = []
        self.status = False
    def getStatus(self):
        return self.status
    #def displayFoodItems(self):