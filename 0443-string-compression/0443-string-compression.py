class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left, right = 0, 1
        cnt = 1
        res = []
        
        while right < len(chars):
            
            if chars[left] == chars[right]:
                cnt += 1
                right += 1
                
            else:
                if cnt == 1:
                    res.append(chars[left])
                else:
                    res.append(chars[left])
                    if len(str(cnt)) > 1:
                        for l in str(cnt):
                            res.append(l)
                    else:
                        res.append(str(cnt))
                left = right
                right += 1
                cnt = 1
        if right - left > 1:
            res.append(chars[left])
            ans = str(right - left)
            if len(str(right - left)) > 1:
                for l in range(len(str(right - left))):
                    res.append(ans[l])
        
            else:
                res.append(str(right - left))
        else:
            res.append(chars[left])
        if len(chars) > len(res):
            for _ in range(len(chars) - len(res)):
                chars.pop()
                
        for i in range(len(res)):
            chars[i] = res[i]
        
        return len(res)
                