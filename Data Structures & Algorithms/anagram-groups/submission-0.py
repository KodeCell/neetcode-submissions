class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            string = ''.join(sorted(s))
            hashmap[string].append(s)
        return list(hashmap.values())
            
        