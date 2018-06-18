class Node:
    def __init__(self, data, left, right, parent, color):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color
    
    def __str__(self):
        return repr(self.data)
    
    
class RedBlackTree:
    def __init__(self):
        self.head = None
        self.depth = 0
    
    
    def left_rotate(self, node):
        new_node = node.right
        node.right = new_node.left
        new_node.left.parent = node
        new_node.parent = node.parent
        if node.parent is None:
            self.root = new_node
        elif node is node.parent.left:
            node.parent.left = new_node
        else:
            node.parent.right = new_node
        new_node.left = node
        node.parent = new_node
                
        
    def append(self, data):
        node = self._append(data)
        print(node)
        new_node = None
        cur = self.head
        while cur is not None:
            new_node = cur
            if node.data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        node.parent = new_node
        if new_node is None:
            self.head = node
        elif node.data < new_node.data:
            new_node.left = node
        else:
            new_node.right = node
        node.left = None
        node.right = None
        node.color = "red"
        self.append_fix(node)
        
        
    def append_fix(self, node):
        while node.parent.color == "red":
            if node.parent is node.parent.parent.left:
                new_node = node.parent.parent.right
                if new_node.color == "red":
                    node.parent.color = "black"
                    new_node.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                elif node is node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.right_rotate(node.parent.parent)
            else:
                new_node = node.parent.parent.right
                if new_node.color == "red":
                    node.parent.color = "black"
                    new_node.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                elif node is node.parent.right:
                    node = node.parent
                    self.right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.left_rotate(node.parent.parent)
            
    def _append(self, data):
        if self.head is None:
            self.head = Node(data, None, None, None, None)
            return self.head
        else:
            cur = self.head
            return self.__append(cur, data)
    
    def __append(self, cur, data):
        if data <= cur.data:
            if cur.left:
                return self.__append(cur.left, data)
            else:
                if cur.right is None:
                    cur.left = Node(data, None, None, cur, None)
                return cur.left
        else:
            if cur.right:
                return self.__append(cur.right, data)
            else:
                if cur.left is None:
                    cur.right = Node(data, None, None, cur, None)
                return cur.right
                
    def print_tree(self):
        if self.head is None:
            print(None)
        else:
            cur = self.head
            self._print_tree(cur)
    
    def _print_tree(self, cur):
        if cur.left:
            self._print_tree(cur.left)
        print(cur)
        if cur.right:
            self._print_tree(cur.right)
            
    def calc_depth(self, cur):
        self.calc_depth(cur.left)
        self.depth += 1
        self.calc_depth(cur.right)
        
tree = RedBlackTree()
for elem in range(10):
    tree.append(elem)

tree.print_tree()
tree.calc_depth(tree.head)
tree.depth
