# Tree

## Definition

- Tree is a data type that is widely used to represent a set of linked nodes, which have a hierarchical structure.
- The topmost node is called the root node. Each node may have child nodes that are subtrees on their own. The nodes that do not have any children are called as Leaf or External nodes.
- Unlike the previous structures that were covered in this video, such as arrays, stacks and queues, a tree is a nonlinear data structure.
- There are different implemetations of the tree structure. This repository includes the foolowing two:
  1. Generic Tree
     - A generic tree refers to the data type in which each node is a data structure that has data and a list of references to its children.
     - Unlike linked list, which each node has one or two references (previous and next), the nodes in a tree may hold multiple references to their children and parent.
     - In a generic tree each node is allowed to have many children and the number of nodes are not known in advance.
     - This kind of a structure is would be a good choice to represent data such as folder structures in a system, where some parent nodes can have multiple children and some can have none.
  2. Binary Tree / Binary Search Tree
     - A subtype of a tree, binary tree defines trees in which each node is allowed to have a maximum of two child nodes.
     - The placement of values can be implemented with a logic to create an rough order. This kind of an implemetnation is called a Binary Search Tree.
       - In the implementation in this repository, when adding children nodes to the root node, the children is placed in the left subtree if it is smaller than the parent.(in the right side otherwise.) This happens recursively in the cases where there are other nodes in the subtrees.
       - This implementation is highly efficient to order and search values. It also does not require a sequential storage for the child nodes (there is only left and right child nodes).
     - Traversing and printing values in a binary tree can be done in a number of ways, that are named based on the positioning of the root node's value.
       1. In-order traversal
          - In-order travelsal, the values of the left-subtree is visited first, followed by the root node and the right subtree values.
          - This representation will return an ordered array in which the root node is placed in its appropriate position.
          - The implemetation in this repositry implements this approach.
       2. Pre-order traversal
          - In pre-order traversal, the root node is placed into the first index of the array. After that the order of left and right tres will be made.
       3. Post-order traversal
          - In post-order traversal, the root node will be placed at the end of the array, after ordering and appending the values in the left and right subtree.

## Common Operations and Their Time Complexities

1. Adding a Child Node
   - Generic Tree = O(1)
     - In generic trees it is possible to add a child to any node.
     - This will simply add the new child into the list of children nodes and takes constant time since it is independent from the number of nodes in the tree.
   - Binary Search Tree = Average case O(log n) Worst Case O(n)
     - Adding a new node into a binary search tree requires traversing through the previously added nodes, do some comparisons and placing the node into its appropriate location.
     - When a binary search tree is balanced, which means there are roughly the same amount of elements in each right and left subtree, adding new nodes take logarithmic time on average, since in each level the amount of values we have to compare is halved.
     - The worst case happens in the cases where all the added values are in an ascending or descending order. In such cases, to add the new node, each previously added node has to be visited once.
       - Example:
         - Root node 100
         - Child 1: 90
         - Child 2: 80
         - Child 3: 70
         - Child 4: 60
           - Each value is added to the left subtree of the previous node. Therefore in each addition, all the previous elements have to be visited.
2. Searching / Removing a Node
   - Generic Tree = O(n)
     - Generic trees are not so efficient in opeartions that require search due to their unordered and uneven structure.
     - In a worst case scenario, all the nodes in a tree have to be visited to find an element and do an operation on.
   - Binary Tree = Average O(log n) / Worst case O(n)
     - Similar to the add operation, the time complexity of an action that involves a search in Binary Search Tree is dependent on the balance of the tree.
     - On average, in a somewhat balanced tree where the distribution of nodes are equal on the left and right subtrees, searching (and deleting) operations take logarithmic time.
     - An uneven tree in which all the values are skewed to one side creates a worst case scenario and increases the complexity to linear time.

## Strengths and Limitations

- Trees are useful data structures that have many types for different use cases.
- Generic trees are good for the representation of data that has a hierarchical order, such as file structures.
- This kind of representation is not possible with a linear or sequential data type.
- The main disadvantages of generic trees are the lack of order and possible uneven distributions of data. This makes it inefficient to search and delete elements within them.
- Binary search trees are very efficient data structures, especially when they are balanced. In those cases the cost of inserting, deleting and looking up values are logarithmic, which is a significant advantage, especially when the tree size is large.
- Binary search tree implements an ordering of the elements. This is a significant advantage over Hash Tables, which have on average better comparative performance on add, lookup and delete opeartions but require extra operations for sorting. Another advantage of the sorted representation is the ability to find the smallest and the largest value in the collection.
- Binary Search Trees are also easier to implement when compared to hash tables, since they do not require a hash function or collusion handling.
- However, as mentioned above a binary search tree's performance is highly dependent on the distribution of data, or its balance. In an unbalanced Binary Search Tree, the cost of performances are higher.

## Real-world Use

- Trees are used in many different forms for solving different problems in programming. Some examples are:
  - Heaps: used for implementing data based on priority. Each node is bigger or smaller than its child nodes. Used for scheduling processes in many operating systems.
  - Generic Trees are used for representing hierarchical data relationships, such as folder structures.
  - In HTML, all the attributes are stored in a tree called Document Object Model (DOM)
  - Binary Search Tree is used in many search applications where data is inserted and removed constantly.
  - Graphs, another tree like structure that is covered in next section, is used for representing collection of nodes that may have non-linear connections, or different link to access each other. In a normal tree, there is only one way of accessing from a child to a parent, while in a graph, there can be many.
