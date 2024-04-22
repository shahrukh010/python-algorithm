class Node(object):
  def __init__(self,data):
    self.data = data;
    self.nextnode = None;

class List:

  def __init__(self):
    self.head = None;
    self.size = 0;
    #tail for adding last element data
    self.tail = None;
    

  def addfirst(self,data):
   self.size = self.size+1;
   newnode = Node(data);
   if not self.head:
     self.head = newnode;
     self.tail = self.head;
   else:
     newnode.nextnode = self.head;
     self.head = newnode;


  def size(self):
    return self.size;

  def size2(self):
    current = self.head;
    total = 0;
    while current is not None:
      total +=1;
      current = current.nextnode;
    return total;

  def addlast(self,data):
    newnode = Node(data);
    if not self.head:
      self.head = newnode;
      self.tail = self.head;
      self.size = self.size+1;
    else:
      self.tail.nextnode = newnode;
      self.tail = newnode;
      self.size +=1;


  def lastdata(self):
    return self.tail.data;


  def remove(self,data):
    if self.head is None:
      return;
    self.size = self.size -1;
    currentnode = self.head;
    previousnode = None;
    while currentnode.data !=data:
      previousnode = currentnode;
      currentnode = currentnode.nextnode;

    if previousnode is None:
       self.head = currentnode.nextnode;
    else:
      previousnode.nextnode = currentnode.nextnode
    
  def __str__(self):
    result = [];
    current = self.head;
    while current is not None:
      result.append(current.data);
      current = current.nextnode;
    return str(result);

    
custom = List()
#custom.addfirst(1);
#custom.addfirst(2);
#custom.addfirst(3);
#custom.addfirst(4);
#custom.addfirst(5);
custom.addlast(10);
custom.addlast(20);
custom.addlast(30);
custom.addlast(40);
custom.addlast(50);
print(custom);
#print(custom.size);
print(custom.size2());
#print(custom.lastdata());
custom.remove(40);
print(custom);
print(custom.size2());


class DoubleList:

  def __init__(self,data):
    self.data = data;
    self.nextnode = None;
    self.previousnode = None;

class DList:
  def __init__(self):
    self.head = None;
    self.tail = None;
    self.size = 0;

  def addElement(self,data):
    newnode = DoubleList(data);
    if not self.head:
      self.head = newnode;
      self.tail = self.head;
    else:
      self.tail.nextnode = newnode;
      newnode.previousnode = self.tail;
      self.tail = newnode;

  def printnode(self):
    current = self.head;
    while current is not None:
      print(current.data);
      current = current.nextnode;

  def printfromlast(self):
    current = self.tail;
    while current is not None:
      print(current.data);
      current = current.previousnode;

d = DList();
d.addElement(100);
d.addElement(200);
d.addElement(300);
d.addElement(400);
d.printnode();
print("print from last doubley list")
d.printfromlast();
