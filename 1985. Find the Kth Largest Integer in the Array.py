class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        temp=list(map(int,nums))
        temp.sort(reverse=True)
        return str(temp[k-1])
            