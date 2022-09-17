class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b , c = 0,0
        s = list(secret)
        g = list(guess)
        i, j = 0,0
        while i < len(secret):
            if s[j] == g[j]:
                b += 1
                s.pop(j)
                g.pop(j)
            else:
                j += 1
            i += 1
        count = Counter(s)
        for l in g:
            if l in count and count[l] > 0:
                c += 1
                count[l] -= 1
        return "{}A{}B".format(b,c)
            