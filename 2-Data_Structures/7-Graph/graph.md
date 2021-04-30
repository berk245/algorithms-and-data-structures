# Graph

## Definition

- Graph is a non-linear data structure consisting of nodes (or vertices) and edges, which refer to the lines that connect nodes in a graph.
- If two nodes are connected with an edge, they are called adjacent nodes.
- The sequence of edges between two nodes are called paths.
- Graph can be called a special kind of tree structure. The main difference is that in trees there is only one path between two nodes, while in a graph there can be many.
- Some common representations of graphs can be names as
  - Adjacency matrix
    - Adjacency Matrix is a 2D array of size V x V where V is the number of vertices/nodes in a graph.
    - It is easy to implement and follow, and removing and looking up for an edge takes constant time.
    - It has V^2 space complexity. Even when there are no edges between nodes, that info has to be represented. Thus making it inefficient, especially for graphs that do not have a lot of edges.
  - Adjacency list
    - In this method, an array (size of nodes or vertices) of linked lists is used.
    - Each node is stored in a list and points to a list of adjacent nodes it connects directly.
    - This representation makes it easy to find successors of a node and more efficient in terms of space.
- To represent a graph as a custom data structure, this repository uses the following logic:
  - Edges are represented as tuples.
  - Based on those tuples, we create a dictionary to store each node.
  - Each node is a key and its value is a set, which consists of its respective edges.
  - With the help of the dictionary, we can then be able to find all paths between two nodes or find the shortest path.
- There are two main types of graphs:
  - An undirected graph refers to one in which the edges do not have directions and indicate a two-way relationship.
  - A directed graph has edges with directions. These graphs can only be traversed in a single direction.
- In some graph implementations, the edges are combined with some information representing a value. These are called weighted graphs.
  - An example could be the flight route planner. There may be many possible options to go from A to B. In such a case, the weight of the edge may represent the prices of those flights, distance between cities, layover times, etc.
  - Based on the algorithm's goal (e.g., returning the cheapest route), that information would be highly crucial.
- Traversing and searching for values
- Graph data structure is part of the graph theory and has many related advanced topics. This repository includes an example of a directed and not weighted graph and demonstrates an algorithm that finds the paths between two nodes.

## Common Operations and Their Time Complexities

- Adding and Deleting a Node = O(1)
  - In the implementation, the nodes in the graph are stored in a dictionary (hash table).
  - On average, lookup, add, and remove operations take linear time.
    - As mentioned in the hash tables markup, depending on collisions the complexity can o up to O(n)
- Adding and Deleting an Edge = O(1)
  - Adding an edge in between two nodes is consisted of two operations:
    - Checking if the start node exists.
    - Adding the destination node to the list of connections.
  - Looking up a value in a dictionary takes constant time on average.
  - A set also uses a hash-table for its underlying data structure. Therefore adding a new element into it takes constant time on average.
- Traverse / Search
  - Graph traversal is the process of visiting each node/vertex in a graph.
  - The process is classified into two categories, based on the order in which nodes are visited.
    - Depth-first search(DFS)
      - In DFS, child vertices are visited before the sibling vertices. The algorithm traverses the depth of any particular path recursively.
      - This method is usually implemented by using a stack, in which the already visited nodes get popped.
    - Breadth-first search(BFS)
      - BFS is another technique that prioritizes visiting the sibling vertices before the child vertices of a node.
      - A queue is often used to track this kind of search process.
  - The time complexity of traversal depends on the technique applied and the graph representation. In adjacency list or dictionary representation;
    - In each technique, visiting a node/vertex takes O(1) time.
    - We then run a for loop on each edge or child node of that node.
    - In the worst case, each node has an edge with every other node in the graph.
    - Therefore each edge is visited two times, (to and from) which takes O(2e) time, where e is the number of edges.
    - We do the same operation on each node (n amount), thus the time complexity becomes O(1 + 2e + n).
    - Since the constants are ignored in Big O analysis, the time complexity of traversal can be written as O(e+n)

## Strengths and Limitations

- Graphs are useful data structures that allow a programmer to store information about the relationship between different entities.
- The ability to store and represent complex relationships and connections provides the ability to build algorithms and solve complex problems, such as shortest path calculation.

## Real-world Use

- Graphs are widely used in many areas and applications. Some can be names as:
  - Route / Flight planning applications
  - Some fingerprint recognition systems translate your fingerprint into a graph
  - Applications that provide suggestions for:
    - Friends you may know
    - Products you might be interested in
  - Search engines
