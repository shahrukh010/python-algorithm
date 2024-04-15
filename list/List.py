
#print the list
list = [1,2,4,5];
print(list);

#replace data on index;
list[2] = 3;
print(list);
#replace from: to
list[0:2] = [10,20,30];
print(list);

#replace interval data;
list[::2] = [3,6,9]
print(list);

#replace every 3rd element.
l = [2,4,6,8,10,12];
l[::2] = [9,11,15];
print(l);

#merge two list
l1 = [10,20,30];
l2 = [40,50,60];
l1.extend(l2);
print(l1);

#concating list
l2 = l2 + [100,101,102];
print(l2);

#check data is present orr not in list
if 300 in l2:
    print("found");
else:
    print("not found");


# traversing list;
for data in l2:
    print(data);

print('otherway to iterate');
for index in range(len(l2)):
    print(l2[index]);

index = 0;
while index !=len(l2):
    print(l2[index]);
    index +=1;

print("reverse list");
#print reverse list.
for index in range(len(l2)-1,-1,-1):
    print(l2[index]);

print("reverse list");
for index in range(-1,-(len(l1)+1),-1):
    print(l1[index]);

#add data into list
l2.append(500);
l2.append(600);
print(l2);

#add  at specfic postion
l2.insert(0,10);
l2.insert(1,20);
l2.insert(2,30);
print(l2);

#copy
l3 = l2.copy();
l3.append(00);
print(l3);

l4 = l3;
l4.append(800);#original object will be effect also.
print(l4);
print(l3);
