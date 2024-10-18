class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    # Initialize two pointers, slow and fast
    slow = head
    fast = head
    
    # Move fast by 2 steps and slow by 1 step until fast reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # When fast reaches the end, slow is at the middle
    return slow

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list from a given node
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Taking input from the user
values = list(map(int, input("Enter the values of the linked list (space-separated): ").split()))

# Create a linked list from the input values
head = create_linked_list(values)

# Find the middle node
middle = middleNode(head)

# Print the result starting from the middle node
print("The linked list from the middle node is:")
print_linked_list(middle)
