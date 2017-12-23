def enqueue(Q,x):
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 1
    else Q.tail = Q.tail + 1

def dequeue(Q):
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 1
    elif Q.head == 0:
        error "Queue Underflow"
    else Q.head = Q.head + 1
    return x
