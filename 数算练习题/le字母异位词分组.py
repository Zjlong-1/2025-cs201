class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())
#或：
#直接二进制加法标记
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di=defaultdict(list)
        for i in strs:
            t=0
            for k in i:
                t+=2**(ord(k)-97)
            di[t].append(i)
        return list(di.values())