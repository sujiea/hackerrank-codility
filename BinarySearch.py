class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
def lca(root, v1, v2):
    low = min(v1, v2)
    high = max(v1, v2)
    v = int(root.info)
    if v >= low and v <= high:
        return root
    else:
        if v > low and v > high:
            return lca(root.left,v1,v2)
        else:
            return lca(root.right,v1,v2)

tree = BinarySearchTree()
t = "8 4 9 1 2 3 6 5"

arr = t.split()

for i in range(len(arr)):
    tree.create(arr[i])

print(lca(tree.root, 1, 2))














