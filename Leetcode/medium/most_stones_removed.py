""" ------- Most Stones Removed with Same Row or Column -------
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, 
return the largest possible number of stones that can be removed.

Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.

Example 3:
Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

Constraints:
    1 <= stones.length <= 1000
    0 <= xi, yi <= 104
    No two stones are at the same coordinate point. """



""" ----- SOLUTION: DFS on union-find ----- 
>>> basically asking for number of islands
define an island as number of points that are connected by row or column. Every point does not have to be next to each other. """
from collections import defaultdict

def removeStones(stones):
    def dfs(i, j):
        points.discard((i,j))
        for y in rows[i]:
            if (i, y) in points:
                dfs(i, y)
        for x in cols[j]:
            if (x, j) in points:
                dfs(x, j)

    points = {(i,j) for i, j in stones}
    
    rows, cols = defaultdict(list), defaultdict(list)
    island = 0
    for i, j in stones:
        rows[i].append(j)
        cols[j].append(i)

    for i, j in stones:
        if (i, j) in points:
            dfs(i, j)
            island += 1
    return len(stones) - island
    # Time: O(N ^ M) where N is the number of stones and M is the number of rows/columns
    # Space: O(N)


stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(removeStones(stones)) # expected output = 5

stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(removeStones(stones)) # expected output = 3

stones = [[0,0]]
print(removeStones(stones)) # expected output = 0