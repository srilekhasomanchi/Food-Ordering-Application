def check_length_less_than(name, n):
    return len(name) <= n

def check_alphabets(s):
    for x in s:
        if((ord(s)>=ord('a') and ord(s)<=ord('z')) or (ord(s)>=ord('A') and ord(s)<=ord('Z'))):
            continue
        return False
    return True

def is_numeric(s):
    for x in s:
        if ((ord(x)) >= ord('0') and ord(x)<=ord('9')):
            continue
        return False
    return True

def is_double(s):
    fl = False
    for x in s:
        if ((ord(x)) >= ord('0') and ord(x)<=ord('9')):
            continue
        elif x == '.':
            if fl or s[-1] == '.':
                return False
            fl = True
            continue
        return False
    return True

def get_hours_minutes_from_time(s):
    hours = 0
    hours += ord(s[0]) - ord('0')
    hours *= 10
    hours += ord(s[1]) - ord('0')
    minutes = 0
    minutes += ord(s[3]) - ord('0')
    minutes *= 10
    minutes += ord(s[4]) - ord('0')
    return (hours,minutes)

def convert_string_to_bool(s):
    if s == "True":
        return True
    else:
        return False

def convert_availability_to_string(val):
    if val:
        return "Available"
    else:
        return "Not available"

class mytime:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def increment(self):
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
            if self.hours == 24:
                self.hours = 0


def are_times_consequent(a,b,c):
    cur = mytime(a.hours,a.minutes)
    while(True):
        if cur.hours == b.hours and cur.minutes == b.minutes:
            return True
        if cur.hours == c.hours and cur.minutes == c.minutes:
            return False
        cur.increment()

def convert_food_ids_to_string(a):
    return(",".join(a))

def convert_string_to_food_ids(s):
    food_ids = []
    cur = ""
    for x in s:
        if x == ',':
            food_ids.append(cur)
            cur = ""
            continue
        cur += x
    food_ids.append(cur)
    return food_ids