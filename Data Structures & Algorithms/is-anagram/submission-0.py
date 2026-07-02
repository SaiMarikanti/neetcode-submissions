class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [0 for i in range(26)]
        s2 = [0 for i in range(26)]

        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            s1[ord(s[i])-97]+=1 
            s2[ord(t[i])-97]+=1 

        for i in range(26):
            if(s1[i]!=s2[i]):
                return False 
        return True       