# Tree

## Definition

- Tree is a widely used data type, that represents a set of linked nodes, which have a hierarchical structure.

- The topmost node is called the root node. Each node may have child nodes that are subtrees on their own. The nodes that do not have any children are called Leaf or External nodes.

- Unlike the previously covered structures in this repository, such as arrays, stacks, and queues, a tree is a nonlinear data structure.
- There are different implementations of the tree structure. This repository includes the following two:
  1. Generic Tree
     - A generic tree refers to the data type in which each node is a data structure that has data and a list of references to its children.
     - Unlike a linked list, in which each node has one or two references (previous and next), the nodes in a tree may hold multiple references to their children and parent.
     - In a generic tree each node is allowed to have many children and the number of nodes is not known in advance.
     - This kind of structure is would be a good choice to represent data such as folder structures in a system, where some parent nodes can have multiple children while some can have none.
  2. Binary Tree / Binary Search Tree
     - A subtype of a tree, binary tree defines trees in which each node is allowed to have a maximum of two child nodes.
     - The values can be placed into the tree with logic to create a rough order. This implementation is called a Binary Search Tree.
       - In the implementation in this repository, when adding children nodes to the root node, the child is placed in the left subtree if it is smaller than the parent. (on the right side otherwise) This procedure happens recursively in the cases where there are other nodes in the subtrees.
       - This implementation is highly efficient to order and search values. It also does not require sequential storage for the child nodes (there are only left and right child nodes).
     - There are three main methods for traversing a binary tree.
       1. In-order traversal
          - In-order traversal, the values of the left-subtree is visited first, followed by the root node and the right subtree values.
          - This representation will return an ordered array in which the root node is placed in its appropriate position.
          - The implementation in this repository implements this approach.
       2. Pre-order traversal
          - In pre-order traversal, the root node is placed into the first index of the array. After that, the left and right trees are ordered.
       3. Post-order traversal
          - In post-order traversal, after ordering and appending the values in the left and right subtree, the root node is placed at the end of the array.

## Common Operations and Their Time Complexities

1. Adding a Child Node
   - Generic Tree = O(1)
     - In generic trees, it is possible to add a child to any node.
     - This will add the new child into the list of children nodes and takes constant time since it is independent of the number of nodes in the tree.
   - Binary Search Tree = Average case O(log n) Worst Case O(n)
     - Adding a new node into a binary search tree requires traversing through the previously added nodes, value comparisons, and placing the node into its appropriate location.
     - When a binary search tree is balanced, which means there are roughly the same amount of elements in each right and left subtree, adding new nodes takes logarithmic time on average since in each level the amount of values we have to compare is halved.
     - The worst-case happens when all the added values are in an ascending or descending order. In such cases, to add the new node, each previously added node has to be visited once.
       - Example:
         - Root node 100
         - Child 1: 90
         - Child 2: 80
         - Child 3: 70
         - Child 4: 60
           - Each value is added to the left subtree of the previous node. Therefore in each addition, all the previous elements have to be visited.
2. Search
   - Generic Tree = O(n)
     - Generic trees are not so efficient in operations that require search due to their unordered and uneven structure.
     - In a worst-case scenario, all the nodes in a tree have to be visited to find an element.
   - Binary Tree = Average O(log n) / Worst case O(n)
     - The time complexity of an action that involves a search in a Binary Search Tree is dependent on the balance of the tree.
     - On average, in a somewhat balanced tree where the distribution of nodes are equal on the left and right subtrees, searching operations take logarithmic time.
     - An uneven tree leads to a worst-case scenario and increases the complexity to linear time.
3. Delete
   - Generic Tree = O(n)
     - In a generic tree, a deletion can be done in linear time in the worst case. Until the matching item/node is found, each item is visited. When the item is found, it is removed from the parent node's children list.
   - Binary Search Tree = O(log n) / Worst case O(n)
     - Deletion in the binary search tree is more complex since it is usually not desired to delete the nodes that follow the node to be deleted.
     - The deletion can be divided into three:
       - When the deleted node has no right or left child
         - This is the simplest scenario, in which the node is simply deleted from the tree.
         - Still requires going through the ordered list of elements and takes logarithmic time on average, and linear time in the worst case.
       - Node with one Child
         - When a node to be deleted has one child, that subtree is moved up one level in the tree.
       - Node with Multiple Children
         - When the node has multiple children, there are two ways to perform the deletion.
           - Popping the minimum value from the right subtree and assigning it to the value of the node to be deleted.
           - Popping the maximum value from the left subtree and assigning it to the value of the node to be deleted.
           - Applying one of these operations will ensure that the order of the tree is accurate after deletion.

## Strengths and Limitations

- Trees are useful data structures that have many types for different use cases.
- Generic trees are good for the representation of data that has a hierarchical order, such as file structures.
- This kind of representation is not possible with a linear or sequential data type.
- The main disadvantages of generic trees are the lack of order and possible uneven distributions of data. This makes it inefficient to search and delete elements within them.
- Binary search trees are very efficient data structures, especially when they are balanced. In those cases, the costs of inserting, deleting, and looking up values are logarithmic, which is a significant advantage, especially when the tree size is large.
- Binary search tree implements an ordering of the elements. This is a significant advantage over Hash Tables, which have on average better comparative performance on add, lookup, and delete operations but require additional operations for sorting. Another advantage of the sorted representation is the ability to find the smallest and the greatest value in the collection.
- Binary Search Trees are also easier to implement compared to hash tables since they do not require a hash function or collusion handling.
- However, as mentioned above, a binary search tree's performance is highly dependent on the distribution of data, or its balance. In an unbalanced Binary Search Tree, the costs of operations are more expensive.

## Real-world Use

- Trees are used in many different forms for solving different problems in programming. Some examples are:
  - Heaps: used for implementing data based on priority. Each node is bigger or smaller than its child nodes. Used for scheduling processes in many operating systems.
  - Generic Trees are used for representing hierarchical data relationships, such as folder structures.
  - In HTML, all the attributes are stored in a tree called Document Object Model (DOM)
  - Binary Search Tree is used in many search applications where data is inserted and removed constantly.
  - Graphs, another tree-like structure that is covered in the next section, is used for representing a collection of nodes that may have non-linear connections, or different links to access each other. In a normal tree, there is only one path between child and parent nodes, while in a graph, there can be many.
