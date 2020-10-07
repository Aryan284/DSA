class Node():
    def __init__(self, val):
        self.data = val
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self, queue):
        if not queue.head:
            return True
        else:
            return False
    
    def create_queue(self, queue):
        if not queue.isEmpty(queue):
            print("\n\nQueue is already created!\n\n")
            return queue
        while True:
            print("Enter -1 to exit.")
            n = int(input("Enter the number to be added in the queue: "))
            if n == -1:
                break
            link_node = Node(n)
            if queue.isEmpty(queue):
                queue.head = link_node
                queue.tail = link_node
            else:
                queue.tail.next = link_node
                queue.tail = link_node
        return queue
    
    def display_queue(self, queue):
        if queue.isEmpty(queue):
            print("\n\nQueue is empty! Cannot display empty queue...\n\n")
            return queue
        disp_node = queue.head
        while disp_node is not None:
            print(disp_node.data, end = " -> ")
            disp_node = disp_node.next
        print("X")
    
    def enqueue(self, queue, n):
        link_node = Node(n)
        if queue.isEmpty(queue):
            queue.head = link_node
            queue.tail = link_node
            return queue
        queue.tail.next = link_node
        queue.tail = link_node
        return queue
    
    def dequeue(self, queue):
        if queue.isEmpty(queue):
            print("\n\nQueue is empty! Cannot dequeue in an empty queue...\n\n")
            return queue
        remove_node = queue.head
        popped_element = queue.head.data
        queue.head = queue.head.next
        remove_node = None
        return popped_element, queue
    
    def stack_using_queues(self, first_queue, second_queue):
        while True:
            print("Enter -1 to exit.")
            n = int(input("Enter the number you want to add: "))
            if n == -1:
                break
            node_link = Node(n)
            second_queue = second_queue.enqueue(second_queue, n)
            while not first_queue.isEmpty(first_queue):
                popped_element, first_queue = first_queue.dequeue(first_queue)
                second_queue = second_queue.enqueue(second_queue, popped_element)
            first_queue, second_queue = second_queue, first_queue
        return first_queue


if __name__=='__main__':
    queue = Queue()
    while True:
        print('Enter -1 to exit')
        print('1. Create a queue.')
        print('2. Display a queue.')
        print('3. Enqueue.')
        print('4. Dequeue.')
        print('5. Implement Stack using Queues.')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            queue = queue.create_queue(queue)
        elif ch == 2:
            queue.display_queue(queue)
        elif ch == 3:
            n = int(input("Enter the number you want to insert in the queue: "))
            queue = queue.enqueue(queue, n)
        elif ch == 4:
            popped_element, queue = queue.dequeue(queue)
        elif ch == 5:
            first_queue = Queue()
            second_queue = Queue()
            first_queue = first_queue.stack_using_queues(first_queue, second_queue)
            first_queue.display_queue(first_queue)
        else:
            break