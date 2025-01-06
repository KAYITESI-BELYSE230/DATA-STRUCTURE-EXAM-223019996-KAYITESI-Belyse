class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full. Cannot add more vehicles.")
            return False

        if self.is_empty():
            self.front = 0
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        print(f"Vehicle {value} parked in slot {self.rear}.")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No vehicles to remove.")
            return None

        vehicle = self.queue[self.front]
        self.queue[self.front] = None

        if self.front == self.rear:
            self.front = self.rear = -1  # Reset the queue if empty
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"Vehicle {vehicle} left the parking slot.")
        return vehicle

    def display(self):
        if self.is_empty():
            print("No vehicles in the parking slots.")
            return

        print("Parking slots status:")
        index = self.front
        while True:
            print(f"Slot {index}: {self.queue[index]}")
            if index == self.rear:
                break
            index = (index + 1) % self.capacity

# Smart Parking System Example
if __name__ == "__main__":
    capacity = 5  # Define the number of parking slots
    parking_queue = CircularQueue(capacity)

    # Simulate parking system
    parking_queue.enqueue("Car-101")
    parking_queue.enqueue("Car-102")
    parking_queue.enqueue("Car-103")
    parking_queue.display()

    parking_queue.dequeue()  # A car leaves
    parking_queue.display()

    parking_queue.enqueue("Car-104")
    parking_queue.enqueue("Car-105")
    parking_queue.enqueue("Car-106")  # Attempt to overfill
    parking_queue.display()

    parking_queue.dequeue()
    parking_queue.dequeue()
    parking_queue.display()
