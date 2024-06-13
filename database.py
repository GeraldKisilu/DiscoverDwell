import sqlite3

# Function to establish a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('discoverdwell.db')
    return conn

# Function to create the necessary tables if they do not already exist
def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Create the hotels table
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

        # Create the rooms table with a foreign key reference to hotels
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

        # Create the transportation table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS transportation (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        )
        ''')

        # Create the hotel_transportation table with foreign key references
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS hotel_transportation (
            id INTEGER PRIMARY KEY,
            hotel_id INTEGER,
            transportation_id INTEGER,
            FOREIGN KEY (hotel_id) REFERENCES hotels (id),
            FOREIGN KEY (transportation_id) REFERENCES transportation (id)
        )
        ''')
        
        # Commit the changes to the database
        conn.commit()
    except sqlite3.Error as e:
        # Print any database errors that occur
        print(f"Database error: {e}")
    finally:
        # Close the database connection
        conn.close()

# Function to insert sample data into the hotels table
def insert_hotels(cursor):
    cursor.execute('''
    INSERT INTO hotels (name, location, continent, price_per_night, max_stay_duration)
    VALUES
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?),
    (?, ?, ?, ?, ?)
    ''', [
        ('Grand Hotel', 'Romania', 'Europe', 120.0, 30),
        ('Beach Resort', 'Romania', 'Europe', 200.0, 15),
        ('Mountain Inn', 'Romania', 'Europe', 80.0, 20),
        ('City Lodge', 'Romania', 'Europe', 100.0, 25),
        ('Country Hotel', 'Romania', 'Europe', 90.0, 10),
        ('Extra Hotel', 'Romania', 'Europe', 110.0, 40)
    ])

# Function to insert sample data into the rooms table
def insert_rooms(cursor):
    cursor.execute('''
    INSERT INTO rooms (hotel_id, room_type, price, availability)
    VALUES
    (?, ?, ?, ?),
    (?, ?, ?, ?),
    (?, ?, ?, ?),
    (?, ?, ?, ?),
    (?, ?, ?, ?),
    (?, ?, ?, ?)
    ''', [
        (1, 'Single', 50.0, 5),
        (1, 'Double', 75.0, 3),
        (2, 'Single', 60.0, 4),
        (3, 'Suite', 150.0, 2),
        (4, 'Single', 55.0, 6),
        (5, 'Double', 70.0, 2)
    ])

# Function to insert sample data into the transportation table
def insert_transportation(cursor):
    cursor.execute('''
    INSERT INTO transportation (name, description)
    VALUES
    (?, ?),
    (?, ?)
    ''', [
        ('Taxi', 'Comfortable and quick'),
        ('Bus', 'Economical and slow')
    ])

# Function to populate the database with sample data
def populate_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Clear existing data from the tables
        cursor.execute('DELETE FROM hotels')
        cursor.execute('DELETE FROM rooms')
        cursor.execute('DELETE FROM transportation')
        cursor.execute('DELETE FROM hotel_transportation')
        
        # Insert sample data into the tables
        insert_hotels(cursor)
        insert_rooms(cursor)
        insert_transportation(cursor)

        # Commit the changes to the database
        conn.commit()
    except sqlite3.Error as e:
        # Print any database errors that occur
        print(f"Database error: {e}")
    finally:
        # Close the database connection
        conn.close()

# Main entry point of the script
if __name__ == '__main__':
    # Create the tables
    create_tables()
    # Populate the tables with sample data
    populate_sample_data()
