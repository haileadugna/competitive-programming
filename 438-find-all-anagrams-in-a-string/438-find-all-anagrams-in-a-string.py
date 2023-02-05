class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # initialize two lists to store the frequency of each letter in string p and the current window of string s
        p_count = [0] * 26
        s_count = [0] * 26
        # calculate the frequency of each letter in string p
        for char in p:
            p_count[ord(char) - ord('a')] += 1
        # initialize an empty list for storing the starting indices of anagrams
        ans = []
        # loop through string s
        for i in range(len(s)):
            # increase the frequency of the current letter in the current window
            s_count[ord(s[i]) - ord('a')] += 1
            # if the current window size is greater than the size of string p
            if i >= len(p):
                # decrease the frequency of the letter that just left the current window
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            # if the frequency of letters in the current window matches the frequency of letters in string p
            if s_count == p_count:
                # append the starting index of the current window to the list of answers
                ans.append(i - len(p) + 1)
        # return the list of starting indices of anagrams
        return ans