class Node:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add_vehicle(self, vehicle_id):
        new_node = Node(vehicle_id)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        print(f"Vehicle {vehicle_id} parked.")

    def remove_vehicle(self, vehicle_id):
        if self.is_empty():
            print("No vehicles in the parking slots.")
            return False

        current = self.head
        while current:
            if current.vehicle_id == vehicle_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                print(f"Vehicle {vehicle_id} left the parking slot.")
                return True
            current = current.next

        print(f"Vehicle {vehicle_id} not found in the parking slots.")
        return False

    def display(self):
        if self.is_empty():
            print("No vehicles in the parking slots.")
            return

        print("Parking slots status:")
        current = self.head
        while current:
            print(f"Vehicle: {current.vehicle_id}")
            current = current.next

# Smart Parking System Example
if __name__ == "__main__":
    parking_list = DoublyLinkedList()

    # Simulate parking system
    parking_list.add_vehicle("Car-101")
    parking_list.add_vehicle("Car-102")
    parking_list.add_vehicle("Car-103")
    parking_list.display()

    parking_list.remove_vehicle("Car-102")  # A car leaves
    parking_list.display()

    parking_list.add_vehicle("Car-104")
    parking_list.add_vehicle("Car-105")
    parking_list.display()

    parking_list.remove_vehicle("Car-101")
    parking_list.remove_vehicle("Car-105")
    parking_list.display()
