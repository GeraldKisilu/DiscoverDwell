from database import get_db_connection

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
