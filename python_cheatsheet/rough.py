class Solution():
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l=0
        r=0
        res=0
        record=[0]*26
        while r<len(s):
            record[ord(s[r])-ord("A")]+=1
            freq=max(record)
            if (r-l+1)-freq<=k:
                res=max(res,(r-l+1))
                r+=1
            

obj=Solution()
obj.characterReplacement("aba",1)
        
        