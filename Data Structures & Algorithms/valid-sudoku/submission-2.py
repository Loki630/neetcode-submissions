class Solution:
    def sortList(self,lst):
        finalList = []
        for item in lst:
            lst1 = [item[i : i + 3] for i in range(0,len(item),3)]
            finalList += lst1
        return finalList

    def checkrowcolumn(self, board):
        for item in board:
            item = [element for element in item if element.isdigit()]
            if sorted(item) == sorted(set(item)):
                pass
            else:
                return False
        for i in range(len(board)):
            lst = [board[j][i] for j in range(len(board[0]))]
            lst = [element for element in lst if element.isdigit()]
            if sorted(lst) == sorted(set(lst)):
                pass
            else:
                return  False
        return True

    def findvalid(self,board):
        for item in [0,9,18]:
            for i in range(item,item + 3):
                lst = []
                for element in board[i : i + 7 : 3]:
                    lst += [item for item in element if item.isdigit()]
                if sorted(lst) == sorted(set(lst)):
                    pass
                else:
                    return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkrowcolumn(board):
            board = self.sortList(board)
            return self.findvalid(board)
        else:
            return False
        