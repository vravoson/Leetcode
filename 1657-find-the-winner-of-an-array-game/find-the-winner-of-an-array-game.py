class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) == 1:
            return arr[0]
        if len(arr) == 2:
            return max(arr)
        if k>=len(arr):
            return max(arr)
        queue = deque(arr)
        curr_winner = queue.popleft()
        count = 0
        
        while count < k:
            challenger = queue.popleft()
            if curr_winner >= challenger:
                count += 1
                queue.append(challenger)
            else:
                queue.append(curr_winner)
                curr_winner = challenger
                count = 1
        
        return curr_winner
