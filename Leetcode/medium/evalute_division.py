""" ------- Evaluate Division -------
You are given an array of variable pairs `equations` and an array of real numbers `values`, 
where `equations[i] = [Ai, Bi]` and `values[i]` represent the equation `Ai / Bi = values[i]`. 

*** Each `Ai` or `Bi` is a string that represents a single variable.

You are also given some queries, where `queries[j] = [Cj, Dj]` represents the jth query where you must find the answer for Cj / Dj = ?.

>>> Return the answers to all queries. If a single answer cannot be determined, return -1.0.

NOTE: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:
Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:
Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:
    1 <= equations.length <= 20
    equations[i].length == 2
    1 <= Ai.length, Bi.length <= 5
    values.length == equations.length
    0.0 < values[i] <= 20.0
    1 <= queries.length <= 20
    queries[i].length == 2
    1 <= Cj.length, Dj.length <= 5
    Ai, Bi, Cj, Dj consist of lower case English letters and digits. """


""" ----- SOLUTION: Graph ----- 
HOW: Each variable can be represented as a node in the graph, 
    and the division relationship between variables can be modeled as edge with direction and weight.
>>> Transform the problem into a path searching problem in a graph
*** Reinterpret the problem as: 
        "given two nodes, we are asked to check if there exists a path between them. 
        If so, we should return the cumulative products along the path as the result.
>>> Use `backtracking`, also known as DFS (Depth-First Search) 
STEP 1) build the graph from list of input equations
STEP 2) Evaluate query one by one via searching the path between the given two variables
        > Handle 2 exception cases:
            - either of the nodes does not exist
            - origin and destination are the same node, i.e `a / a` and result os one """

from collections import defaultdict

def calcEquation(equations, values, queries):
    
    graph = defaultdict(defaultdict)

    def backtrack_evaluate(curr_node, target_node, acc_product, visited):
        visited.add(curr_node)
        ret = -1.0
        neighbors = graph[curr_node]
        if target_node in neighbors:
            ret = acc_product * neighbors[target_node]
        else:
            for neighbor, value in neighbors.items():
                if neighbor in visited:
                    continue
                ret = backtrack_evaluate(
                    neighbor, target_node, acc_product * value, visited)
                if ret != -1.0:
                    break
        visited.remove(curr_node)
        return ret

    # Step 1) built the graph
    for (dividend, divisor), value in zip(equations, values):
        graph[dividend][divisor] = value
        graph[divisor][dividend] = 1 / value
    
    # Step 2) Evalute each query by backtracking (DFS) - verify if there's a path from divisor
    results = []
    for dividend, divisor, in queries:
        if dividend not in graph or divisor not in graph:
            # exception case #1
            ret = -1.0
        elif dividend == divisor:
            # exception case #2
            ret = 1.0
        else:
            visited = set()
            ret = backtrack_evaluate(dividend, divisor, 1, visited)
        results.append(ret)

    return results
    # Time: O(M * N)
    # Space: O(N)

equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# expected output = [6.00000,0.50000,-1.00000,1.00000,-1.00000]
print(calcEquation(equations, values, queries)) 


equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# expected output = [3.75000,0.40000,5.00000,0.20000]
print(calcEquation(equations, values, queries)) 


equations = [["a","b"]]
values = [0.5]
queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# expected output = [0.50000,2.00000,-1.00000,-1.00000]
print(calcEquation(equations, values, queries)) 