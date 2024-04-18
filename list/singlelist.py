
class Node:
    def __init__(self,value=None):
        self.value = value;
        self.next = None;

class singlelist:
    def __init__(self):
        self.head = None;
        self.tail = None;

    def __str__(self):

        result = [];
        while self.head:
            result.append(self.head.value);
            self.head = self.head.next;
        return str(result)




list = singlelist();
node1 = Node(1);
node2 = Node(2);
node3 = Node(3);
node4 = Node(4);
node5 = Node(5);

#this implementation takes only o(1) to add data to list.
list.head = node1;
list.head.next = node2;
list.head.next.next = node3;
list.head.next.next.next = node4;
list.head.next.next.next.next = node5;
list.tail = node5;

print(list);



#other way to create single list

class NodeList:
    def __init__(self,value = None):
        self.value = value;
        self.next = None;


class List:
    def __init__(self):
        self.head = None;
        self.tail = None;


    def add(self,value):
        node = NodeList(value);

        if self.head is None:
            self.head = node;
            self.tail = self.head;
        else:
            self.tail.next = node;
            self.tail = node;

    def addat(self,index,data=None):

        if index == 0:
            node = NodeList(data);
            tmp = self.head;
            print(tmp.value);
            node.next = tmp;
            self.head = node;
        else:
            node = NodeList(data);
            tmp = self.head;
            for i in range(index-2):
                tmp = tmp.next;
            rnode = tmp.next;
            tmp.next = node;
            node.next = rnode;



    def __str__(self):

        result =[];
        while self.head:
            result.append(self.head.value);
            self.head = self.head.next;
        return str(result);


new_node = List();
new_node.add(10);
new_node.add(20);
new_node.add(30);
#new_node.add(40);
#new_node.add(50);
print('printing all the node');
print(new_node);

print('after adding at position');
new_node.addat(0,25);
print(new_node);
