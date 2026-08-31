class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_letter = dict()
        for word in strs:
            count = [0] * 26
            for char in word:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

            if key not in word_letter:
                word_letter[key] = [word]
            else:
                word_letter[key].append(word)

        return list(word_letter.values())