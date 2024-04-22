
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