class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            s_ = ''.join(sorted(s))
            if s_ not in d:
                d[s_] = [s]
            else:
                d[s_].append(s)
        return list(d.values())