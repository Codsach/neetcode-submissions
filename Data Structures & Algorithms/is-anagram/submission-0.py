class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}

        for char in s:
            if char in frequency:
                frequency[char]+=1
            else:
                frequency[char]=1
        
        for char in t:
            if char in frequency:
                frequency[char]-=1
            else:
                return False
        return all(count == 0 for count in frequency.values())
        
