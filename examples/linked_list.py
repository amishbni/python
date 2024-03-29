class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        next = str(self.next.data) if self.next else "null"
        return f"{self.data} -> {next}"


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, previous_node, data):
        if previous_node is None:
            raise ValueError("Previous node doesn't exist.")
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def swap_by_value(self, first, second):
        if first == second:
            return

        first_previous = None
        first_current = self.head
        while first_current and first_current.data != first:
            first_previous = first_current
            first_current = first_current.next

        second_previous = None
        second_current = self.head
        while second_current and second_current.data != second:
            second_previous = second_current
            second_current = second_current.next

        if first_current is None or second_current is None:
            return

        if first_previous is None:
            self.head = second_current
        else:
            first_previous.next = second_current

        if second_previous is None:
            self.head = first_current
        else:
            second_previous.next = first_current

        first_current.next, second_current.next = second_current.next, first_current.next

    def swap_by_position(self, first, second):
        if first == second:
            return

        first_previous = None
        first_current = self.head
        first_position = 0
        while first_current and first_position != first:
            first_previous = first_current
            first_current = first_current.next
            first_position += 1

        second_previous = None
        second_current = self.head
        second_position = 0
        while second_current and second_position != second:
            second_previous = second_current
            second_current = second_current.next
            second_position += 1

        if first_current is None or second_current is None:
            return

        if first_previous is None:
            self.head = second_current
        else:
            first_previous.next = second_current

        if second_previous is None:
            self.head = first_current
        else:
            second_previous.next = first_current

        first_current.next, second_current.next = second_current.next, first_current.next


    def delete_by_value(self, value):
        current_node = self.head
        if current_node and current_node.data == value:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        while current_node and current_node.data != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def delete_by_position(self, position):
        current_node = self.head
        if position == 0:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        current_position = 0
        while current_node and current_position != position:
            previous_node = current_node
            current_node = current_node.next
            current_position += 1

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def reverse(self):
        previous_node = None
        current_node = self.head

        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

    def recursive_reverse(self):
        def _recursive_reverse(previous_node, current_node):
            if current_node is None:
                return previous_node
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            return _recursive_reverse(previous_node, current_node)
        self.head = _recursive_reverse(previous_node=None, current_node=self.head)

    def merge(self, linked_list):
        first_current = self.head
        second_current = linked_list.head
        smallest = None

        if first_current is None:
            return second_current
        if second_current is None:
            return first_current

        if first_current.data <= second_current.data:
            smallest = first_current
            first_current = smallest.next
        else:
            smallest = second_current
            second_current = smallest.next
        new_head = smallest

        while first_current and second_current:
            if first_current.data <= second_current.data:
                smallest.next = first_current
                smallest = first_current
                first_current = smallest.next
            else:
                smallest.next = second_current
                smallest = second_current
                second_current = smallest.next

        if first_current is None:
            smallest.next = second_current
        if second_current is None:
            smallest.next = first_current

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        current_node = self.head
        previous_node = None
        if current_node is None:
            return
        unique_values = set()
        while current_node:
            if current_node.data in unique_values:
                previous_node.next = current_node.next
            else:
                unique_values.add(current_node.data)
                previous_node = current_node
            current_node = current_node.next

    def print(self, end='\n'):
        current_node = self.head
        while current_node:
            if current_node.next:
                end_character = ', '
            else:
                end_character = end
            print(current_node.data, end=end_character)
            current_node = current_node.next

    def length(self) -> int:
        current_node = self.head
        count = 0
        while current_node:
            current_node = current_node.next
            count += 1

        return count

    def recursive_length(self, node) -> int:
        if node is None:
            return 0
        return 1 + self.recursive_length(node.next)


if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}")
    singly_linked_list.print()
    singly_linked_list.append(1)
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.prepend(7)
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.append(5)
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.append(3)
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.append(4)
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.append(4)
    print(f"len={singly_linked_list.recursive_length(singly_linked_list.head)}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.prepend(0)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.insert(singly_linked_list.head.next.next, 100)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.delete_by_value(5)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.delete_by_position(3)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.swap_by_value(0, 3)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.swap_by_position(1, 4)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.reverse()
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.recursive_reverse()
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()

    first_list = SinglyLinkedList()
    first_list.append(1)
    first_list.append(3)
    first_list.append(5)
    first_list.append(10)

    second_list = SinglyLinkedList()
    second_list.append(2)
    second_list.append(6)
    second_list.append(7)

    first_list.merge(second_list)
    print(f"len={first_list.length()}", end=' -> ')
    first_list.print()

    singly_linked_list.append(3)
    singly_linked_list.append(1)
    singly_linked_list.append(7)
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
    singly_linked_list.remove_duplicates()
    print(f"len={singly_linked_list.length()}", end=' -> ')
    singly_linked_list.print()
