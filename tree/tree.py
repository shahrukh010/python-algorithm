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