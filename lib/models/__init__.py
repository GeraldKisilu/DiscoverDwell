from lib.helpers import get_db_connection

class Hotel:
    def __init__(self, id, name, location, continent, price_per_night, max_stay_duration):
        self.id = id
        self.name = name
        self.location = location
        self.continent = continent
        self.price_per_night = price_per_night
        self.max_stay_duration = max_stay_duration

    @property
    def room_count(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM rooms WHERE hotel_id = ?', (self.id,))
        count = cursor.fetchone()[0]
        conn.close()
        return count

class Room:
    def __init__(self, id, hotel_id, room_type, price, availability):
        self.id = id
        self.hotel_id = hotel_id
        self.room_type = room_type
        self.price = price
        self.availability = availability

class Transportation:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

class HotelTransportation:
    def __init__(self, id, hotel_id, transportation_id):
        self.id = id
        self.hotel_id = hotel_id
        self.transportation_id = transportation_id

# Functions to interact with the database
def add_hotel(name, location, continent, price_per_night, max_stay_duration):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO hotels (name, location, continent, price_per_night, max_stay_duration)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, location, continent, price_per_night, max_stay_duration))
    conn.commit()
    conn.close()

def get_hotels_by_location(location):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM hotels WHERE location = ? LIMIT 5
    ''', (location,))
    hotels_data = cursor.fetchall()
    conn.close()
    return [Hotel(*hotel) for hotel in hotels_data]

def add_room(hotel_id, room_type, price, availability):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO rooms (hotel_id, room_type, price, availability)
    VALUES (?, ?, ?, ?)
    ''', (hotel_id, room_type, price, availability))
    conn.commit()
    conn.close()

def get_rooms_by_hotel(hotel_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM rooms WHERE hotel_id = ?
    ''', (hotel_id,))
    rooms_data = cursor.fetchall()
    conn.close()
    return [Room(*room) for room in rooms_data]

def add_transportation(name, description):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO transportation (name, description)
    VALUES (?, ?)
    ''', (name, description))
    conn.commit()
    conn.close()

def get_transportation():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM transportation')
    transportation_data = cursor.fetchall()
    conn.close()
    return [Transportation(*transport) for transport in transportation_data]

def book_hotel(hotel_id, transportation_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO hotel_transportation (hotel_id, transportation_id)
    VALUES (?, ?)
    ''', (hotel_id, transportation_id))
    conn.commit()
    conn.close()
