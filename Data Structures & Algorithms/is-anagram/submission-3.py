class Solution:
    def isAnagram(self, s:str , t:str)-> bool:
        frequency = {}

        for i in s:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        for i in t:
            if i in frequency:
                frequency[i] -= 1
            else:
                return False
        return all(count ==  0 for count in frequency.values())