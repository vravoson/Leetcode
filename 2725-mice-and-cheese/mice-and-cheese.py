class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        if k==0:
            return sum(reward2)
        diff_reward = [reward1[i] - reward2[i] for i in range(n)]
        reward_diff, position = zip(*sorted(zip(diff_reward, range(n))))
        res = sum([reward1[x] for x in position[-k:]]) # mouse 1
        res += sum([reward2[x] for x in position[:-k]]) # mouse 2
        return res
        