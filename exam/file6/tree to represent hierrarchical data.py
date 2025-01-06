class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

# Example Usage: Hierarchical Smart Parking System
if __name__ == "__main__":
    # Root node for the parking system
    parking_system = TreeNode("Parking System")

    # Adding zones
    zone_a = TreeNode("Zone A")
    zone_b = TreeNode("Zone B")
    parking_system.add_child(zone_a)
    parking_system.add_child(zone_b)

    # Adding floors to zones
    floor_a1 = TreeNode("Floor A1")
    floor_a2 = TreeNode("Floor A2")
    zone_a.add_child(floor_a1)
    zone_a.add_child(floor_a2)

    floor_b1 = TreeNode("Floor B1")
    floor_b2 = TreeNode("Floor B2")
    zone_b.add_child(floor_b1)
    zone_b.add_child(floor_b2)

    # Adding parking slots to floors
    slot_a1_1 = TreeNode("Slot A1-1")
    slot_a1_2 = TreeNode("Slot A1-2")
    floor_a1.add_child(slot_a1_1)
    floor_a1.add_child(slot_a1_2)

    slot_b1_1 = TreeNode("Slot B1-1")
    slot_b1_2 = TreeNode("Slot B1-2")
    floor_b1.add_child(slot_b1_1)
    floor_b1.add_child(slot_b1_2)

    # Display the hierarchical structure
    print("Hierarchical Structure of the Smart Parking System:")
    parking_system.display()
