class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, x):
        """Add an element to the end of the queue."""
        self.queue.append(x)
        print(f"Enqueued Element = {x}")
        print("Queue:", self.queue, "\n")
    
    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.isempty():
            print("Queue is Empty, can't dequeues elements\n")
        else:
            print(f"Dequeued Element = {self.queue[0]}")
            self.queue.pop(0)
            print("Remaining Queue:", self.queue, "\n")
        
    def peek(self):
        """View the front element of the queue."""
        if self.isempty():
            print("Queue is Empty, can't peek\n")
        else:
            print(f"Front of the queue = {self.queue[0]}")
            print("Queue:", self.queue, "\n")
        
    def isempty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

# Example usage
q1 = Queue()
q1.enqueue(30)
q1.enqueue(50)
q1.enqueue(5)
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.enqueue(11)
q1.enqueue(25)
q1.peek()
q1.dequeue()
q1.dequeue()
q1.peek()