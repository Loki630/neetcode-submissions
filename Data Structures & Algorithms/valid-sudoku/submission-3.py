class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                
                item = board[r][c]
                
                if item.isdigit() != True:
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)
                if item in rows[r] or item in columns[c] or item in boxes[box_index] :
                    return False
                rows[r].add(item)
                columns[c].add(item)
                boxes[box_index].add(item)
        
        return True
        