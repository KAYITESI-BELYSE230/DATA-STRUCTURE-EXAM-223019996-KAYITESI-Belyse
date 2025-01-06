class ParkingSpot:
    def __init__(self, spot_id, location, availability, priority):
        self.spot_id = spot_id
        self.location = location
        self.availability = availability  # True if available, False if occupied
        self.priority = priority  # Priority score (1-10, 10 being highest)
    
    def __str__(self):
        status = "Available" if self.availability else "Occupied"
        return f"Spot ID: {self.spot_id} | Location: {self.location} | Status: {status} | Priority: {self.priority}"

def selection_sort_parking(parking_spots):
    n = len(parking_spots)
    
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            # Sort based on priority (higher priority comes first)
            if parking_spots[j].priority > parking_spots[max_idx].priority:
                max_idx = j
        
        # Swap the found maximum element with the first element
        parking_spots[i], parking_spots[max_idx] = parking_spots[max_idx], parking_spots[i]
    
    return parking_spots

def get_user_input():
    parking_spots = []
    
    while True:
        try:
            num_spots = int(input("Enter the number of parking spots to manage: "))
            if num_spots <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    for i in range(num_spots):
        print(f"\nEntering data for parking spot {i+1}")
        
        spot_id = input("Enter Spot ID: ")
        location = input("Enter Location: ")
        
        while True:
            availability = input("Is the spot available? (yes/no): ").lower()
            if availability in ['yes', 'no']:
                availability = True if availability == 'yes' else False
                break
            print("Please enter 'yes' or 'no'")
        
        while True:
            try:
                priority = int(input("Enter Priority (1-10, 10 being highest): "))
                if 1 <= priority <= 10:
                    break
                print("Priority must be between 1 and 10")
            except ValueError:
                print("Please enter a valid number")
        
        parking_spot = ParkingSpot(spot_id, location, availability, priority)
        parking_spots.append(parking_spot)
    
    return parking_spots

def main():
    print("Smart Parking System - Data Entry and Sorting")
    print("===========================================")
    
    # Get parking spots data from user
    parking_spots = get_user_input()
    
    print("\nUnsorted Parking Spots:")
    print("----------------------")
    for spot in parking_spots:
        print(spot)
    
    # Sort parking spots using selection sort
    sorted_spots = selection_sort_parking(parking_spots)
    
    print("\nSorted Parking Spots (by Priority):")
    print("----------------------------------")
    for spot in sorted_spots:
        print(spot)

if __name__ == "__main__":
    main()