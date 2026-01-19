# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''

    def __init__(self, name):
        self.name = name
        self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist")

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            print(f"{name} added to the end of the waitlist")
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        print(f"{name} added to the end of the waitlist")

    def remove(self, name):
        if self.head is None:
            print(f"{name} not found")
            return

        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist")
            return

        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                print(f"Removed {name} from the waitlist")
                return
            current = current.next

        print(f"{name} not found")

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    # Create a new linked list instance
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            print("Current waitlist:")
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")


# Call the waitlist_generator function to start the program
waitlist_generator()


"""
Design Memo

This linked list works by storing each customer as a node that points to the next customer in line. Each node holds a customer’s name and a reference to the next node. The list starts with a head, which is the first customer on the waitlist. When someone is added or removed, the program updates the pointers between nodes instead of using a regular Python list. This allows the list to change size easily as customers are added or removed.

The head plays a very important role because it is the entry point to the entire list. Every operation starts from the head. When a customer is added to the front, the head changes to the new node. When the first customer is removed, the head is updated to the next node in the list. Without the head, the program would not know where the list begins or how to access the rest of the customers.

A real engineer might need a custom linked list like this when they want more control over how data is stored and changed. Linked lists are useful when data needs to be added or removed often, especially from the beginning or middle of a list. In real systems like waitlists, queues, or scheduling tools, using a linked list can be more efficient and flexible than using built-in lists. This project helped me understand how linked lists work behind the scenes and how they can be used in real-world applications.
"""
