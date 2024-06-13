from lib.models import get_hotels_by_location, get_rooms_by_hotel, get_transportation, book_hotel

# Function to display a list of hotels with their details
def display_hotels(hotels_list):
    for hotel in hotels_list:
        print(f"ID: {hotel.id}, Name: {hotel.name}, Location: {hotel.location}, Continent: {hotel.continent}, Price per Night: {hotel.price_per_night}, Max Stay Duration: {hotel.max_stay_duration}, Rooms: {hotel.room_count}")

# Function to display a list of rooms with their details
def display_rooms(rooms_list):
    for room in rooms_list:
        print(f"ID: {room.id}, Room Type: {room.room_type}, Price: {room.price}, Availability: {room.availability}")

# Function to display a list of transportation options with their details
def display_transportation(transportation_list):
    for transport in transportation_list:
        print(f"ID: {transport.id}, Name: {transport.name}, Description: {transport.description}")

# Function to search for hotels based on user input for continent and country
def search_hotels():
    continent = input("Enter the continent (Europe, Africa, Asia, America, UAE): ").strip()
    country = input("Enter the country: ").strip()
    
    # Fetch hotels based on the country
    hotels_list = get_hotels_by_location(country)
    
    # Debug print statement to identify hotels found
    print(f"Debug: Found {len(hotels_list)} hotels in {country}")
    
    if hotels_list:
        print("\nAvailable Hotels:")
        display_hotels(hotels_list)
        view_rooms(hotels_list)
    else:
        print("No hotels found for the specified location.")

# Function to view rooms of a selected hotel
def view_rooms(hotels_list):
    hotel_id = int(input("\nEnter the ID of the hotel to view rooms: "))
    
    # Fetch rooms based on the selected hotel
    rooms_list = get_rooms_by_hotel(hotel_id)
    
    # Debug print statement to identify rooms found
    print(f"Debug: Found {len(rooms_list)} rooms in hotel ID {hotel_id}")
    
    if rooms_list:
        print("\nAvailable Rooms:")
        display_rooms(rooms_list)
        book_selected_room(hotels_list, rooms_list)
    else:
        print("No rooms found for the selected hotel.")

# Function to book a selected room in a hotel
def book_selected_room(hotels_list, rooms_list):
    room_id = int(input("\nEnter the ID of the room you want to book: "))
    duration = int(input("Enter the duration of stay (in days): "))
    
    # Get the hotel ID from the room details
    hotel_id = rooms_list[room_id-1].hotel_id
    
    # Check if the duration exceeds the maximum stay duration
    if duration > hotels_list[hotel_id-1].max_stay_duration:
        print("Duration exceeds the maximum stay duration for the selected hotel.")
        return
    
    # Fetch available transportation options
    transportation_list = get_transportation()
    print("\nAvailable Transportation:")
    display_transportation(transportation_list)
    
    transportation_id = int(input("\nEnter the ID of the transportation you want to book: "))
    
    # Book the hotel and room along with the selected transportation
    book_hotel(hotel_id, transportation_id)
    print("Hotel and room booked successfully!")

# Main menu function to navigate through the application
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

# Entry point of the script
if __name__ == '__main__':
    main_menu()
