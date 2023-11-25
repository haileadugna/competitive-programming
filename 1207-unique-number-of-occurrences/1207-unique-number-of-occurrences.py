class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp = Counter(arr)
        ans = temp.values()
        if len(ans) == len(set(ans)):
            return True
        else:
            return False