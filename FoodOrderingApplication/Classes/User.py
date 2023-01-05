class User:
    def __init__(self, userId, name, phoneNumber):
        self.userId = userId
        self.name = name
        self.phoneNumber = phoneNumber
    def editDetails(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber