class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # convert strings s and p to lists
        s = list(s)
        p = list(p)
        # create a Counter object for string p
        tmp = Counter(p)
        # set initial values for pointers l and r
        l, r= 0, len(p)
        # initialize an empty list for storing the starting indices of anagrams
        ans = []
        # loop through the string s, until r pointer goes past the end
        while r <= len(s):
            # create a Counter object for the current substring s[l:r]
            temp = Counter(s[l:r])
            # check if the Counter objects of p and s[l:r] match
            if tmp == temp:
                # if they match, append the starting index l to the list of answers
                ans.append(l)
            # move both pointers to the right by one character
            l += 1
            r += 1
        # return the list of starting indices of anagrams
        return ans