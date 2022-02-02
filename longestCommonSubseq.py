class Solution:
    def printMatrix(self, data):
        for row in data:
            for elem in row:
                print(elem, end=' ')
            print()

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)]
              for i in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        #self.printMatrix(dp)
        return dp[0][0]

    def canVisitAllRooms(self, rooms):
        stack = []
        visited = [False] * len(rooms)
        visited[0] = True
        for key in rooms[0]:
            stack.append(key)
            visited[key] = True

        while (stack):
            key = stack.pop()
            for key in rooms[key]:
          
                if visited[key] != True:
                    print('appended')
                    stack.append(key)
                    visited[key] = True

        return True if all(visited) else False

    
# file = open('trie.py','r')
# print("Output of Readlines after appending")
# line = file.readlines()
# print(line[0])
# file.close()

sol = Solution()
# print(sol.longestCommonSubsequence('abcde','ace'))

print(sol.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0, 2]]))

