class Stack_structure:
    def __init__(self):
        self.q = Queue_structure()
    def check_empty(self):
        return self.q.check_empty()
    def push_val(self, data):
        self.q.enqueue_operation(data)
    def pop_val(self):
        for _ in range(self.q.size_calculate() - 1):
            dequeued = self.q.dequeue_operation()
            self.q.enqueue_operation(dequeued)
        return self.q.dequeue_operation()
class Queue_structure:
    def __init__(self):
        self.items = []
        self.size = 0
    def check_empty(self):
        return self.items == []
    def enqueue_operation(self, data):
        self.size += 1
        self.items.append(data)
    def dequeue_operation(self):
        self.size -= 1
        return self.items.pop(0)
    def size_calculate(self):
        return self.size
my_instance = Stack_structure()

while True:
    print('Menu')
    print('push <value>')
    print('pop')
    print('quit')

    my_input = input('What operation would you like to perform ? ').split()
    operation = my_input[0].strip().lower()
    if operation == 'push':
        my_instance.push_val(int(my_input[1]))
    elif operation == 'pop':
        if my_instance.check_empty():
            print('The stack is empty.')
        else:
            print('The deleted value is : ', my_instance.pop_val())
    elif operation == 'quit':
        break