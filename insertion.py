

# 4.2
# 4.4
# 4.5
# 4.8
# 4.10
# 4.11

# #        A
# #      /   \
# #     B     C
# #    / \   /
# #   D   E F

# graph = {'A': ['B', 'C'],
#          'B': ['D', 'E'],
#          'C': ['F'],
#          'D': [''],
#          'E': [''],
#          'F': [''],
#          }


# def search(Node root) {
#     if (root == nUll) return;
#         visit(root);
#         root. visited = true;
#         for each(Node n in root. adjacent) {
#             if (n.visited == false) {
#                 search(n);}
#         }
#     }


# void search(Node root) {
#     Queue queue = new Queue();
#     root.marked = true;
#     queue.enqueue(root); II Add to the end of queue

#     while (!queue.isEmpty({
#         Node r=queue.dequeue(); II Remove from the front of the queue
#         visit(r);
#         foreach(Node n in r.adjacent) {
#             if (n.marked == false) {
#                 n.marked=true;
#                 queue.enqueue(n);}
#     }
#     }

class Node: 
    def __init__(self, d): 
        self.data = d 
        self.left = None
        self.right = None
  
# function to convert sorted array to a 
# balanced BST 
# input : sorted array of integers 
# output: root node of balanced BST 
def sortedArrayToBST(arr): 
      
    if not arr: 
        return None
  
    # find middle 
    mid = (len(arr)) // 2
      
    # make the middle element the root 
    root = Node(arr[mid]) 
      
    # left subtree of root has all 
    # values <arr[mid] 
    root.left = sortedArrayToBST(arr[:mid]) 
      
    # right subtree of root has all  
    # values >arr[mid] 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 
  
# A utility function to print the preorder  
# traversal of the BST 
def preOrder(node): 
    if not node: 
        return
      
    print(node.data)
    preOrder(node.left) 
    preOrder(node.right)  
  
# driver program to test above function 
""" 
Constructed balanced BST is  
    4 
/ \ 
2 6 
/ \ / \ 
1 3 5 7 
"""
  
arr = [1, 2, 3, 4, 5, 6, 7] 
root = sortedArrayToBST(arr) 
# preOrder(root) 
  