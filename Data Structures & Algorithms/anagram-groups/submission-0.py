class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            s = i
            ch_array = [0 for i in range(26)]
            for j in s:
                ch_array[97-ord(j)]+=1 
            if tuple(ch_array) in dic:
                dic[tuple(ch_array)].append(s)
            else:
                dic[tuple(ch_array)] = [s]

        ans = []
        for i in dic:
            ans.append(dic[i])
        return ans
            
        