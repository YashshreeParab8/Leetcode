# Find Most Frequent Vowel and Consonant and return their sum
# Skilli daily challenge 
class Solution:
    def maxFreqSum(self, s: str) -> int:
        counts={}
        for ch in s:
            counts[ch]=counts.get(ch,0)+1
        vowels = 'aeiouAEIOU'
        max_vowel=0
        max_consonant=0
        for ch, freq in counts.items():
            if ch in vowels:
                max_vowel = max(max_vowel,freq)
            else:
                max_consonant = max(max_consonant,freq)
            
        return max_consonant + max_vowel