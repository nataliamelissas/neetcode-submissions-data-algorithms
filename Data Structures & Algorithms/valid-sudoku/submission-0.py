class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        LENGTH = 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # check rows
        for i in range(LENGTH):
            curr_row = set()
            for j in range(LENGTH):
                num = board[i][j]

                if num == '.':
                    continue

                # add to squares
                square_key = (i // 3, j // 3)

                if (num in rows[i] or num in cols[j] or num in squares[square_key]):
                    return False

                rows[i].add(num)
                cols[j].add(num)
                squares[square_key].add(num)

        return True
                