class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        dictt = {"small":0, "capital":0}
        for letter in word:
            if 122 >= ord(letter) >= 97 :
                dictt["small"] +=1
            else:
                dictt["capital"] += 1
        if dictt["capital"] == len(word) or dictt["small"] == len(word):
            return True
        elif dictt["capital"] == 1 and ord(word[0]) < 97:
            return True
        else:
            return False
            