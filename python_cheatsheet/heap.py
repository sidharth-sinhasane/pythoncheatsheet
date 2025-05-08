import heapq
# defolt is min heap
# under hood is list only
myheap=[6,3,6,83,7,4,7]
heapq.heapify(myheap)
heapq.heappush(myheap,5) #log(n)

min = heapq.heappop(myheap) #log(n)

h2=[1,2,3,4,5]
heapq.heapify(h2)

h3=heapq.merge(h2,myheap) # merge two heaps
print(h3) # this is a generator

print(myheap)

# for max heap multiply by -1
