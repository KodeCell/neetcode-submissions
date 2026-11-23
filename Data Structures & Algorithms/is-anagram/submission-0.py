class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        for ch in s:
            freqs[ch] = freqs.get(ch, 0)+1
        freqt = {}
        for ch in t:
            freqt[ch] = freqt.get(ch, 0) + 1
        return (freqs == freqt)

        