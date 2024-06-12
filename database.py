import sqlite3

def get_db_connection():
    conn = sqlite3.connect('discoverdwell.db')
    return conn

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotels (
        id INTEGER PRIMARY KEY,
        name TEXT,
        location TEXT,
        continent TEXT,
        price_per_night REAL,
        max_stay_duration INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        hotel_id INTEGER,
        room_type TEXT,
        price REAL,
        availability INTEGER,
        FOREIGN KEY (hotel_id) REFERENCES hotels (id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transportation (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hotel_transportation (
        id INTEGER PRIMARY KEY,
        hotel_id INTEGER,
        transportation_id INTEGER,
        FOREIGN KEY (hotel_id) REFERENCES hotels (id),
        FOREIGN KEY (transportation_id) REFERENCES transportation (id)
    )
    ''')

    conn.commit()
    conn.close()

def populate_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM hotels')
    cursor.execute('DELETE FROM rooms')
    cursor.execute('DELETE FROM transportation')
    cursor.execute('DELETE FROM hotel_transportation')

    cursor.execute('''
    INSERT INTO hotels (name, location, continent, price_per_night, max_stay_duration)
    VALUES
    ('Grand Hotel', 'Romania', 'Europe', 120.0, 30),
    ('Beach Resort', 'Romania', 'Europe', 200.0, 15),
    ('Mountain Inn', 'Romania', 'Europe', 80.0, 20),
    ('City Lodge', 'Romania', 'Europe', 100.0, 25),
    ('Country Hotel', 'Romania', 'Europe', 90.0, 10),
    ('Extra Hotel', 'Romania', 'Europe', 110.0, 40)
    ''')

    cursor.execute('''
    INSERT INTO rooms (hotel_id, room_type, price, availability)
    VALUES
    (1, 'Single', 50.0, 5),
    (1, 'Double', 75.0, 3),
    (2, 'Single', 60.0, 4),
    (3, 'Suite', 150.0, 2),
    (4, 'Single', 55.0, 6),
    (5, 'Double', 70.0, 2)
    ''')

    cursor.execute('''
    INSERT INTO transportation (name, description)
    VALUES
    ('Taxi', 'Comfortable and quick'),
    ('Bus', 'Economical and slow')
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tables()
    populate_sample_data()
