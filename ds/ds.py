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
