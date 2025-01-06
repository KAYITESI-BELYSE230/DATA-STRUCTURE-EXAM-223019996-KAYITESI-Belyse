class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, order):
        if self.is_full():
            print("Queue is full. Cannot add more orders.")
            return False

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = order
        self.size += 1
        print(f"Order {order} added to the queue.")
        return True

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. No orders to process.")
            return None

        order = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"Order {order} processed and removed from the queue.")
        return order

    def display(self):
        if self.is_empty():
            print("No orders in the queue.")
            return

        print("Current orders in the queue:")
        index = self.front
        for _ in range(self.size):
            print(f"Order: {self.queue[index]}")
            index = (index + 1) % self.capacity

# Smart Parking System Order Management Example
if __name__ == "__main__":
    capacity = int(input("Enter the maximum number of orders the queue can hold: "))
    order_queue = Queue(capacity)

    while True:
        print("\nOptions:")
        print("1. Add an order")
        print("2. Process an order")
        print("3. Display orders")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            order = input("Enter the order ID to add: ")
            order_queue.enqueue(order)
        elif choice == '2':
            order_queue.dequeue()
        elif choice == '3':
            order_queue.display()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
