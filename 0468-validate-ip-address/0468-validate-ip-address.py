class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if "." in queryIP:
            nums = queryIP.split('.')
            for x in nums:
        
                if len(x) == 0 or len(x) > 3:
                    return "Neither"
           
                if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                    return "Neither"
                
            if queryIP.count(".") == 3:
                return "IPv4"
        
        elif ":" in queryIP:
            nums = queryIP.split(':')
            hexdigits = '0123456789abcdefABCDEF'
            for x in nums:
            
                if len(x) == 0 or len(x) > 4 or not all(c in hexdigits for c in x):
                    return "Neither"
                
            if queryIP.count(":") == 7:
                
                return "IPv6"
                        
        return 'Neither'
                