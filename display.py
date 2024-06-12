import models

def display_hotels(hotels_list):
    for hotel in hotels_list:
        print(f"ID: {hotel.id}, Name: {hotel.name}, Location: {hotel.location}, Continent: {hotel.continent}, Price per Night: {hotel.price_per_night}, Max Stay Duration: {hotel.max_stay_duration}, Rooms: {hotel.room_count}")

def display_rooms(rooms_list):
    for room in rooms_list:
        print(f"ID: {room.id}, Room Type: {room.room_type}, Price: {room.price}, Availability: {room.availability}")

def display_transportation(transportation_list):
    for transport in transportation_list:
        print(f"ID: {transport.id}, Name: {transport.name}, Description: {transport.description}")

def search_hotels():
    continent = input("Enter the continent (Europe, Africa, Asia, America, UAE): ").strip()
    country = input("Enter the country: ").strip()
    hotels_list = models.get_hotels_by_location(country)
    # Debug print statements to  identify hotels
    print(f"Debug: Found {len(hotels_list)} hotels in {country}")
    if hotels_list:
        print("\nAvailable Hotels:")
        display_hotels(hotels_list)
        view_rooms(hotels_list)
    else:
        print("No hotels found for the specified location.")

def view_rooms(hotels_list):
    hotel_id = int(input("\nEnter the ID of the hotel to view rooms: "))
    rooms_list = models.get_rooms_by_hotel(hotel_id)
    print(f"Debug: Found {len(rooms_list)} rooms in hotel ID {hotel_id}")
    if rooms_list:
        print("\nAvailable Rooms:")
        display_rooms(rooms_list)
        book_hotel(hotels_list, rooms_list)
    else:
        print("No rooms found for the selected hotel.")

def book_hotel(hotels_list, rooms_list):
    room_id = int(input("\nEnter the ID of the room you want to book: "))
    duration = int(input("Enter the duration of stay (in days): "))
    hotel_id = rooms_list[room_id-1].hotel_id
    if duration > hotels_list[hotel_id-1].max_stay_duration:
        print("Duration exceeds the maximum stay duration for the selected hotel.")
        return
    
    transportation_list = models.get_transportation()
    print("\nAvailable Transportation:")
    display_transportation(transportation_list)
    
    transportation_id = int(input("\nEnter the ID of the transportation you want to book: "))
    models.book_hotel(hotel_id, transportation_id)
    print("Hotel and room booked successfully!")

def main_menu():
    while True:
        print("\nDiscoverDwell - Hotel Hunting")
        print("1. Search for Hotels")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            search_hotels()
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")
