class Solution(object):
    def findWord(self,ind,i,j,board,word,m,n,visited):
        if ind==len(word):
            return True
        flag=False
        #hor_right
        if j+1<n:
            if ((i,j+1) not in visited) and board[i][j+1]==word[ind]:
                visited.add((i,j+1))
                flag=self.findWord(ind+1,i,j+1,board,word,m,n,visited)
                visited.remove((i,j+1))
        if flag:
            return True
        #hor_left
        if j-1>-1:
            if ((i,j-1) not in visited) and  board[i][j-1]==word[ind]:
                visited.add((i,j-1))
                flag=self.findWord(ind+1,i,j-1,board,word,m,n,visited)
                visited.remove((i,j-1))
        if flag:
            return True
        #ver_up
        if i-1>-1:
            if ((i-1,j) not in visited) and  board[i-1][j]==word[ind]:
                visited.add((i-1,j))
                flag=self.findWord(ind+1,i-1,j,board,word,m,n,visited)
                visited.remove((i-1,j))
        if flag:
            return True
        #ver_down
        if i+1<m :
            if ((i+1,j) not in visited) and  board[i+1][j]==word[ind]:
                visited.add((i+1,j))
                flag=self.findWord(ind+1,i+1,j,board,word,m,n,visited)
                visited.remove((i+1,j))
        if flag:
            return True
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m=len(board)
        n=len(board[0])
        visited=set()
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited.add((i,j))
                    flag=self.findWord(1,i,j,board,word,m,n,visited)
                    visited.remove((i,j))
                    if flag:
                        return True
        return False
        
