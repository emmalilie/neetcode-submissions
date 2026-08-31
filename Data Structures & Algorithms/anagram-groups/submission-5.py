class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_letter = dict()
        for idx in range(len(strs)):
            count = [0] * 26
            for char in strs[idx]:
                index = ord(char) - ord("a")
                count[index] += 1
            
            key = tuple(count)

            if key not in word_letter:
                word_letter[key] = [idx]
            else:
                word_letter[key].append(idx)

        final = []
        for key in word_letter:
            group = []
            for idx in word_letter[key]:
                group.append(strs[idx])
            
            final.append(group)

        return final
    


