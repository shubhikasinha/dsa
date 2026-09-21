import re

class Solution:
    def numDifferentIntegers(self, word):
        cleaned_word = re.sub(r'[^0-9]', ' ', word)
        
        unique_integers = set()
        
        for s in cleaned_word.split():
            unique_integers.add(int(s))
            
        return len(unique_integers)