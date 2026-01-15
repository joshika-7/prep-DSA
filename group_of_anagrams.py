from typing import List
from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)    #i still dont know what edge case we are solving here
        for s in strs:
            count = 26 * [0]
            for c in s:
                count[ord(c) - ord("a")] += 1   #create a count array for each string so if c = e, ord(e)-ord(a) is 4, so count[4]=1 so like we create count
            res[tuple(count)].append(s)    #we hash map it here - since list cant be a key ive used tuples as they are immutable

        print(res)
        return list(res.values())

obj = Solution()
ans = obj.groupAnagrams(strs=["act","pots","hat"])
print(ans)