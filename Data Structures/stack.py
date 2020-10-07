class Node():
    def __init__(self, val):
        self.data = val
        self.next = None
    
class Stack():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def create_stack(self, stack):
        if stack.head:
            print('\n\nStack is already created!\n')
            return stack
        while True:
            print('\n\nEnter -1 to exit.')
            n = int(input('Enter the number you want to insert: '))
            if n == -1:
                break
            push_link = Node(n)
            if not stack.head:
                stack.head = push_link
                stack.tail = push_link
            else:
                push_link.next = stack.head
                stack.head = push_link
        return stack
    
    def display_stack(self, stack):
        if not stack.head:
            print('Stack is empty. Cannot display empty stack!')
            return stack
        disp_link = stack.head
        while disp_link is not None:
            print('|', disp_link.data, '|', end = "\n")
            disp_link = disp_link.next
        print('  X')
    
    def push(self, stack):
#         if not stack.head:
#             print('Stack is empty. Cannot push in empty stack!')
#             return stack
        n = int(input('Enter the number you want to push: '))
        push_link = Node(n)
        push_link.next = stack.head
        stack.head = push_link
        return stack
    
    def pop(self, stack):
        if not stack.head:
            print('Stack is empty. Cannot pop in empty stack!')
            return stack
        popped_element = stack.head.data
        pop_link = stack.head
        stack.head = stack.head.next
        pop_link = None
        return popped_element, stack

if __name__=='__main__':
    stack = Stack()
    while True:
        print('Enter -1 to exit.')
        print('1. Create a stack.')
        print('2. Display a stack.')
        print('3. Push an element.')
        print('4. Pop an element.')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            stack = stack.create_stack(stack)
        elif ch == 2:
            stack.display_stack(stack)
        elif ch == 3:
            stack = stack.push(stack)
        elif ch == 4:
            popped_element, stack = stack.pop(stack)
        else:
            break