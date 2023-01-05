import MySQLdb as mdb
#from mysql.connector import Error
import numpy as np

class DataBase:
    def __init__(self):
        try:
            self.database = mdb.connect('localhost', 'root', 'Srilekha', 'Somanchi@2001')

            cursor = self.database.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                                email varchar(50) PRIMARY KEY,
                                                password varchar(40),
                                                name varchar(100),
                                                contact varchar(10),
                                                address varchar(200),
                                                area_id varchar(10))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS restaurants (
                                                restaurant_id varchar(50) PRIMARY KEY,
                                                manager_email varchar(50),
                                                name varchar(100),
                                                opening_time varchar(5),
                                                closing_time varchar(5),
                                                address varchar(200),
                                                area_id varchar(10),
                                                phone varchar(10),
                                                flag varchar(5))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS cart(
                                                item_id varchar(10) PRIMARY KEY,
                                                food_id varchar(10),
                                                user_email varchar(50))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS food_items(
                                                food_id varchar(50) PRIMARY KEY,
                                                restaurant_id varchar(50),
                                                name varchar(50),
                                                description varchar(300),
                                                availability varchar(5),
                                                price double
                                                )''')


            cursor.execute('''CREATE TABLE IF NOT EXISTS areas(
                                                area_id varchar(10) PRIMARY KEY,
                                                name varchar(100),
                                                city varchar(100))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS orders(
                                                order_id varchar(10) PRIMARY KEY,
                                                food_items varchar(500),
                                                customer_email varchar(50),
                                                status varchar(20),
                                                delivery_person_email varchar(50),
                                                city varchar(100))''')

            cursor = self.database.cursor()
            cursor.execute("select * from areas")
            data = cursor.fetchall()

            if len(data) == 0:
                areas = dict()
                areas['Hyderabad'] = ['Uppal', 'Madhapur', 'Banjara Hills', 'Ameerpet'
                    , 'Begumpet', 'Somajiguda', 'Gachibowli', 'Manikonda',
                                      'Miyapur', 'Kondapur']
                areas['Guntur'] = ['Lakshmipuram', 'Brodipet', 'Arundelpet', 'Chandramouli Nagar',
                                   'Brindavan Gardens', 'Koritepadu', 'Pattabhipuram', 'Old town',
                                   'Vidya Nagar', 'Nagaraly']
                areas['Vizag'] = ['Akkayapalem','Kapuluppada','China Gadili','Madhurawada',
                                  'Boyapalem','MVP Colony', 'Desaparthrunipalem']


                for x in areas.keys():
                    for y in areas[x]:
                        area_id = ""
                        for i in range(5):
                            area_id += (chr(np.random.randint(ord('0'),ord('9')+1)))
                        cursor.execute("INSERT into areas (area_id,name,city) values ('{0}','{1}','{2}')".format(area_id,y,x))
                        self.database.commit()



        except Exception as error:
            print(error)

    
    def user_login(self, email, password):
        cursor = self.database.cursor()
        cursor.execute("select * from users where email='"+email+"' and password='"+password+"'")
        data = cursor.fetchall()
        cursor.close()
        if len(data) > 0:
            return True
        else:
            return False

    def insert_user(self, name, email, password, contact):
        cursor = self.database.cursor()
        cursor.execute("select * from users where email = '{0}'".format(email))
        data = cursor.fetchall()
        if len(data) != 0:
            return False
        cursor.execute("select * from users where contact = '{0}'".format(contact))
        data = cursor.fetchall()
        val = (email, password, name, contact)
        if len(data) != 0:
            return False
        cursor.execute("INSERT into users (email,password,name,contact) values (%s,%s,%s,%s)", val)
        self.database.commit()
        cursor.close()
        return True

    def get_user_details(self, email):
        cursor = self.database.cursor()
        cursor.execute("select name, contact, address, area_id from users where email = '{0}'".format(email))
        data = cursor.fetchall()
        if len(data) == 0:
            return False
        else:
            return data[0]

    def get_restaurant_details_managed_by(self, email):
        cursor = self.database.cursor()
        cursor.execute("select * from restaurants where manager_email = '{0}'".format(email))
        data = cursor.fetchall()
        if len(data) == 0:
            return None
        else:
            return data[0]

    def get_all_cities(self):
        cursor = self.database.cursor()
        cursor.execute("select distinct city from areas")
        data = cursor.fetchall()
        result = []
        for x in data:
            result.append(x[0])
        return result

    def get_areas_in_city(self,city):
        cursor = self.database.cursor()
        cursor.execute("select name from areas where city = '{0}'".format(city))
        data = cursor.fetchall()
        result = []
        for x in data:
            result.append(x[0])
        return result

    def insert_restaurant(self,manager_email,name,opening_time,closing_time,address,area,city,phone):
        cursor = self.database.cursor()
        id = ""
        for i in range(10):
            id += (chr(np.random.randint(ord('0'), ord('9') + 1)))
        cursor.execute("select area_id from areas where city = '{0}' and name = '{1}'".format(city,area))
        data = cursor.fetchall()
        area_id = data[0][0]
        cursor.execute("select * from restaurants where name = '{0}' and area_id = '{1}'".format(name,area_id))
        data = cursor.fetchall()
        if len(data) > 0:
            return 1
        cursor.execute("select * from restaurants where phone = '{0}'".format(phone))
        data = cursor.fetchall()
        if len(data) > 0:
            return 2

        cursor.execute("INSERT into restaurants (restaurant_id,manager_email,name,opening_time,closing_time,address,area_id,phone,flag) values ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','False')".format(id,manager_email,name,opening_time,closing_time,address,area_id,phone))
        self.database.commit()

    def insert_food_item(self,restaurant_id,name,description,price):
        cursor = self.database.cursor()
        id = ""
        for i in range(10):
            id += (chr(np.random.randint(ord('0'), ord('9') + 1)))
        cursor.execute("INSERT into food_items (food_id, restaurant_id, name, description, availability, price) values ('{0}','{1}','{2}','{3}','False',{4})".format(id, restaurant_id, name, description, price))
        self.database.commit()

    def get_food_items(self, restaurant_id):
        cursor = self.database.cursor()
        cursor.execute("select * from food_items where restaurant_id = '{0}'".format(restaurant_id))
        data = cursor.fetchall()
        return data

    def switch_availability(self, food_id, value):
        cursor = self.database.cursor()
        cursor.execute("UPDATE food_items SET availability = '{0}' where food_id = '{1}'".format(value, food_id))
        self.database.commit()

    def edit_food_item(self, id, name, description, price, availability):
        cursor = self.database.cursor()
        cursor.execute("UPDATE food_items SET name = '{0}', description = '{1}', price = {2}, availability = '{3}' where food_id = '{4}'".format(name, description, price, availability, id))
        self.database.commit()

    def update_user_area(self, email, address, area, city):
        cursor = self.database.cursor()

        cursor.execute("select area_id from areas where city = '{0}' and name = '{1}'".format(city, area))
        data = cursor.fetchall()
        area_id = data[0][0]

        cursor.execute(
            "update users set address = '" + address + "', area_id = '" + area_id + "' where email = '" + email + "'")

        self.database.commit()
        cursor.close()
        return 1

    def city_by_areaid(self, areaid):
        cursor = self.database.cursor()
        cursor.execute("select city from areas where area_id = '" + areaid + "'")
        data = cursor.fetchall()
        return data[0][0]

    def get_area_by_areaid(self, areaid):
        cursor = self.database.cursor()
        cursor.execute("select name from areas where area_id = '{0}'".format(areaid))
        data = cursor.fetchall()
        return data[0][0]

    def restaurants_by_city(self, area_id):
        cursor = self.database.cursor()
        user_city = self.city_by_areaid(area_id)
        cursor.execute("select * from restaurants left outer join areas on restaurants.area_id = areas.area_id where areas.city = '{0}'".format(user_city))
        data = cursor.fetchall()
        return data

    def update_user_profile(self, email, name, mobile, address, area, city):
        cursor = self.database.cursor()
        self.update_user_area(email, address, area, city)
        cursor.execute(
            "update users set name = '" + name + "', contact = '" + mobile + "' where email = '" + email + "'")
        self.database.commit()
        cursor.close()
        return 1

    def delete_food_item(self, food_id):
        cursor = self.database.cursor()
        cursor.execute("delete from food_items where food_id = '{0}'".format(food_id))
        self.database.commit()
        cursor.close()

    def add_to_cart(self, user_email, food_id):
        cursor = self.database.cursor()
        id = ""
        for i in range(10):
            id += (chr(np.random.randint(ord('0'), ord('9') + 1)))
        cursor.execute("INSERT into cart (item_id, user_email, food_id) values ('{0}','{1}','{2}')".format(id, user_email, food_id))
        self.database.commit()
        cursor.close()

    def get_user_cart_items(self, user_email):
        cursor = self.database.cursor()
        cursor.execute("select * from cart where user_email = '{0}'".format(user_email))
        data = cursor.fetchall()
        return data

    def get_food_item_by_id(self, food_id):
        cursor = self.database.cursor()
        cursor.execute("select * from food_items where food_id = '{0}'".format(food_id))
        data = cursor.fetchall()
        return data[0]

    def remove_from_cart(self, item_id):
        cursor = self.database.cursor()
        cursor.execute("delete from cart where item_id = '{0}'".format(item_id))
        self.database.commit()

    def update_user_city(self, email, area, city):
        cursor = self.database.cursor()

        cursor.execute("select area_id from areas where city = '{0}' and name = '{1}'".format(city, area))
        data = cursor.fetchall()
        area_id = data[0][0]

        cursor.execute(
            "update users set area_id = '" + area_id + "' where email = '" + email + "'")

        self.database.commit()
        cursor.close()
        return 1

    def is_mobile_number_exists(self, mobile):
        cursor = self.database.cursor()
        cursor.execute("select * from users where contact = '{0}'".format(mobile))
        data = cursor.fetchall()
        if len(data) > 0:
            return True
        return False

    def insert_order(self, customer_email, food_ids, city):
        cursor = self.database.cursor()
        id = ""
        for i in range(10):
            id += (chr(np.random.randint(ord('0'), ord('9') + 1)))
        cursor.execute("INSERT INTO orders (order_id, food_items, customer_email, status, city) values ('{0}','{1}','{2}','{3}','{4}')".format(id, food_ids, customer_email, "Being Prepared", city))
        self.database.commit()
    def remove_item_from_cart(self, item_id):
        cursor = self.database.cursor()
        cursor.execute("delete from cart where item_id = '{0}'".format(item_id))
        self.database.commit()

    def remove_from_cart(self, customer_email):
        cursor = self.database.cursor()
        cursor.execute("delete from cart where user_email = '{0}'".format(customer_email))
        self.database.commit()

    def get_areaid_by_restaurant_id(self, restaurant_id):
        cursor = self.database.cursor()
        cursor.execute("select area_id from restaurants where restaurant_id = '{0}'".format(restaurant_id))
        data = cursor.fetchall()
        return data[0][0]

    def get_orders_for_delivery_by_city(self, city):
        cursor = self.database.cursor()
        cursor.execute("select * from orders where city = '{0}' and delivery_person_email is NULL".format(city))
        data = cursor.fetchall()
        return data

    def get_restaurant_name_from_id(self, restaurant_id):
        cursor = self.database.cursor()
        cursor.execute("select name from restaurants where restaurant_id = '{0}'".format(restaurant_id))
        data = cursor.fetchall()
        return data[0][0]

    def get_areaid_by_user_email(self, user_email):
        cursor = self.database.cursor()
        cursor.execute("select area_id from users where email = '{0}'".format(user_email))
        data = cursor.fetchall()
        return data[0][0]

    def set_delivery_person(self, order_id, delivery_email):
        cursor = self.database.cursor()
        cursor.execute("update orders set delivery_person_email = '{0}' where order_id = '{1}'".format(delivery_email, order_id))
        self.database.commit()

    def get_orders_by_delivery_email(self, email):
        cursor = self.database.cursor()
        cursor.execute("select * from orders where delivery_person_email = '{0}'".format(email))
        data = cursor.fetchall()
        return data

    def get_address_by_restaurant_id(self, restaurant_id):
        cursor = self.database.cursor()
        cursor.execute("select address from restaurants where restaurant_id = '{0}'".format(restaurant_id))
        data = cursor.fetchall()
        return data[0][0]

    def get_address_by_email(self, email):
        cursor = self.database.cursor()
        cursor.execute("select address from users where email = '{0}'".format(email))
        data = cursor.fetchall()
        return data[0][0]

    def update_status(self, order_id, status):
        cursor = self.database.cursor()
        cursor.execute("update orders set status = '{0}' where order_id = '{1}'".format(status, order_id))
        self.database.commit()

    def get_orders_by_user_email(self, email):
        cursor = self.database.cursor()
        cursor.execute("select * from orders where customer_email = '{0}'".format(email))
        data = cursor.fetchall()
        return data