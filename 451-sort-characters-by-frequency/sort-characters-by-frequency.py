class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s)
        return ''.join(char * count for char, count in frequency.most_common())