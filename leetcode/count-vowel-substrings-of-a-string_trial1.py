class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        count = 0
        word_length = len(word)
      
        for start_index in range(word_length):
            found_vowels = set()          
            for char in word[start_index:]:
                if char not in vowels:
                    break              
                found_vowels.add(char)
              
                if len(found_vowels) == 5:
                    count += 1
      
        return count