class Node(object):
  def __init__(self,data):
    self.data = data;
    self.leftchild = None;
    self.rightchild = None;

class BinarySearchTree(object):
  def __init__(self):
    self.root = None;

  def getNode(self):
    return self.root;
    
  def add(self,data):
    node = Node(data);
    if not self.root:
      self.root = node;
    else:
      self.insertNode(data,self.root);

  def insertNode(self,data,node):

    if data < node.data:
      if node.leftchild:
        self.insertNode(data,node.leftchild);
      else:
        node.leftchild = Node(data);
    else:
      if node.rightchild:
        self.insertNode(data,node.rightchild);
      else:
        node.rightchild = Node(data);

  def getMinValue(self):
    if self.root:
      return self.__getMin__value(self.root);

  def __getMin__value(self,node):
    if node.leftchild:
      return self.__getMin__value(node.leftchild);
    return node.data;

  def getMaxValue(self):
    if self.root:
      return self.__getMax__(self.root);

  def __getMax__(self,node):
    if node.rightchild:
      return self.__getMax__(node.rightchild);
    return node.data;

  def inorder_iterative(self,node):
    if node is None:
      return;
    result = [];
    stack = [];
    while len(stack) !=0 or node is not None:
      if node:
        stack.append(node);
        node = node.leftchild;
      else:
        tmp = stack.pop();
        result.append(tmp);
        node = tmp.rightchild;
    return result;

    
  def inorder(self,node):
    if node :
      self.inorder(node.leftchild);
      print(node.data);
      self.inorder(node.rightchild);


tree = BinarySearchTree();
tree.add(8)
tree.add(3)
tree.add(1)
tree.add(10);
tree.add(14);
tree.add(13)
tree.inorder(tree.getNode());
#node = tree.getNode();
print(tree.getMinValue());
print(tree.getMaxValue());
result = tree.inorder_iterative(tree.getNode());
for data in result:
  print(data.data,end=',')
print();

print();
print('*'*3,'change the data',"*"*3);


class Tree:
  def __init__(self,data):
    self.data = data;
    self.leftchild = None;
    self.rightchild = None;

  def preorder(self,node):
    if node is None:
      return;
    result = [];
    stack = [];
    while node is not None or len(stack) !=0:
      if node:
        result.append(node.data)
        stack.append(node)
        node = node.leftchild;
      else:
        tmp = stack.pop();
        node = tmp.rightchild;
    return result;
    
t = Tree("A")
t.leftchild = Tree("B");
t.leftchild.leftchild = Tree("D");
t.leftchild.rightchild = Tree("E");
t.rightchild = Tree("C");
t.rightchild.rightchild = Tree("G");
t.rightchild.leftchild = Tree("F");

result = t.preorder(t);
for data in result:
  print(data);

