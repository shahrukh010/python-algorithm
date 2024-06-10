from collections import Counter

#create a list
L = ['hector','annie','bridget','nic','hector','annie','bridget','hector']

#Get the occurence of L
c = Counter(L);#it will return dictonary
print(c);
for key in c:
  print(key,c[key]);

#Get the specific occreance of element
print(c['annie']);

#Get the element or key only
for ele in c.elements():
  print(ele);

#drop the data
c.pop('nic');
print(c);
#print(c.popitem());
print(c.most_common());

#deque operation
from collections import deque
L = [1,2,3,5];
d = deque(L)
d.append(6)
d.appendleft(0)
print(d)
print(L);
d.pop();
print(d);
d.popleft();
print(d);
d.extend([10,20,30])
print(d);


#working with array
import array;

input = array.array('i',[10,20,30,40,50])
#'i'->Integer
print(input);
arr = b"ABCDEF"
#b -> byte
input = array.array('b',arr);
print(input);
print(input[0],input[2])
print(dir(arr));
input.append(100)
print(input);


#working on heapq

import heapq;
H = [];

heapq.heappush(H,10);
heapq.heappush(H,30);
heapq.heappush(H,50);
heapq.heappush(H,20)
print(H);
heapq.heappop(H);
print(H)

#make L to heap
L = [40,20,10,30,50];

heapq.heapify(L)
print(L);

print(heapq.nlargest(3,L));
print(heapq.nsmallest(2,L))


def sayHello():
  return "hello";
