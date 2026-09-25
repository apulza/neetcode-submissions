class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False
        
        count = [0] * 26  # Array for 26 lowercase English letters
        
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
            
        # Check if all counts are zero
        for val in count:
            if val != 0:
                return False
                
        return True