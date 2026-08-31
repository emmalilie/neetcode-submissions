class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_map = dict()
        for index in range(len(strs)):
            letter = tuple(sorted(strs[index]))
            if letter not in sorted_map:
                sorted_map[letter] = [index]
            else:
                sorted_map[letter].append(index)
        
        final = []
        for key in sorted_map:
            group = []
            for index in sorted_map[key]:
                group.append(strs[index])
            final.append(group)

        return final

        

        