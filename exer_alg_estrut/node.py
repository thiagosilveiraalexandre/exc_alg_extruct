class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        self.prev = None
    
    def get_data(self):
        return self.data
    
    def set_data(self, new_data):
        self.data = new_data
    
    def __str__(self):
        return str(self.data)

def insert_in_order(head, new_data):
    new_node = Node(new_data)
    
    if head is None:
        head = new_node
        return head
    
    if new_node.data < head.data:
        new_node.next = head
        head.prev = new_node
        head = new_node
        return head
    
    current = head
    
    if new_node.data == current.data:
        print("the value", new_node.data,"already exists in the list. type in the list")
        return head 
    
    while current.next is not None and current.next.data < new_node.data:
        current = current.next
        
    new_node.next = current.next
     
    
    if current.next is not None:
        current.next.prev = new_node
        
    current.next = new_node
    new_node.prev = current
    
    return head

def imprimir_normal(head):
    if head is None:
        print("List null")
    else:
        current = head
        while current is not None:
            print(current.data)
            current = current.next
    print("List:", head)

head = None

while True:
    try:
        value = int(input("insert element: "))
        head = insert_in_order(head, value)
    except ValueError:
        break



    imprimir_normal(head)

def imprimirReverso(head):
    if head is None:
        print("is null")
    else:
        current = head
        while current.next is not None:
            current = current.next 
        
        imprimirReversoRecursivo(current)

def imprimirReversoRecursivo(node):
    if node is not None:
        print(node.data)
        imprimirReversoRecursivo(node.prev)

imprimirReverso(head)
