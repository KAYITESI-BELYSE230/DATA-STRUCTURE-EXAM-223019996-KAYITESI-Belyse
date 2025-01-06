class DynamicArray:
    def __init__(self):
        self.array = []

    def add_vehicle(self, vehicle_id):
        self.array.append(vehicle_id)
        print(f"Vehicle {vehicle_id} parked.")

    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.array:
            self.array.remove(vehicle_id)
            print(f"Vehicle {vehicle_id} left the parking slot.")
        else:
            print(f"Vehicle {vehicle_id} not found in the parking slots.")

    def display(self):
        if not self.array:
            print("No vehicles in the parking slots.")
        else:
            print("Current vehicles in the parking slots:")
            for vehicle in self.array:
                print(f"Vehicle: {vehicle}")

# Smart Parking System using Dynamic Array
if __name__ == "__main__":
    parking_system = DynamicArray()

    while True:
        print("\nOptions:")
        print("1. Park a vehicle")
        print("2. Remove a vehicle")
        print("3. Display parked vehicles")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            vehicle_id = input("Enter the vehicle ID to park: ")
            parking_system.add_vehicle(vehicle_id)
        elif choice == '2':
            vehicle_id = input("Enter the vehicle ID to remove: ")
            parking_system.remove_vehicle(vehicle_id)
        elif choice == '3':
            parking_system.display()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
