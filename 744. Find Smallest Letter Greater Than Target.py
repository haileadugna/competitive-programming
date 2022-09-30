class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s, e = 0, len(letters)-1
        while s <= e:
            mid = (s + e)//2
            if letters[mid] <= target:
                s = mid + 1
            else:
                e = mid -1
        print(s)
        if s == len(letters):
            return letters[0]
        else:
            return letters[s]