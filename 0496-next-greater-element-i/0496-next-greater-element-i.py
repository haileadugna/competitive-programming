class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        greater = defaultdict( lambda: -1)
        monostack = []
        
        for num in nums2:
            
            while monostack and num > monostack[-1]:
                greater[monostack.pop()] = num
            monostack.append(num)
        
        return [greater[num] for num in nums1]