from collections import deque

q=deque()
q.append(1)    #element is added
q.append(6)    #1,6
print(q)

#queue is created
q.popleft()  #6
print(q)

#stack is created
q.append(4)  #6,4
q.pop()  #6
print(q)