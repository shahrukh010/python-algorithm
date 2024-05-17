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