class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def insert_at_front(data, head):
    old_head = head
    new_head = Node(data=data, next_node=old_head)
    return new_head

def insert_at_end(data, head):
    end = Node(data=data)
    p = head

    while p.next_node != None:
        p = p.next_node
    p.next_node = end
    return head

def insert_at_index(data, head, index):
    count = 0
    if index == 0:
        return insert_at_front(data, head)
    else:
        current = head
        while count != index:
            prev = current
            current = current.next_node
            count += 1
        new = Node(data=data, next_node=current)
        prev.next_node = new
        return head

def remove_first_node(head):
    head = head.next_node
    return head

def remove_last_node(head):
    p = head

    while p.next_node:
        n = p
        p = n.next_node
    n.next_node = None
    return head

def remove_at_index(head, index):
    count = 0
    if index == 0:
        return remove_first_node(head)
    else:
        current = head
        while count != index:
            prev = current
            current = current.next_node
            count += 1
    prev.next_node = current.next_node
    return head

def reverse_linked_list(head):
    p = head
    reverse = Node()

    while p != None:
        second = p.next_node
        p.next_node = reverse
        reverse = p
        p = second

    return reverse

def travel_forward(head):
    if not head:
        return
    else:
        print(head.data)
        travel_forward(head.next_node)

def travel_backward(head):
    if not head:
        return
    else:
        travel_backward(head.next_node)
        print(head.data)

if __name__ == '__main__':
    a = Node()
    b = Node()
    c = Node()

    a.data = 'First'
    a.next_node = b

    b.data = 'Second'
    b.next_node = c

    c.data = 'Third'

    new = insert_at_front("woop", a)

    head = remove_first_node(new)

    head = insert_at_end('last', head)
    head = remove_last_node(head)
    head = insert_at_index("testing", head, 3)
    head = remove_at_index(head, 3)

    travel_forward(head)

    head = reverse_linked_list(head)

    travel_forward(head)
