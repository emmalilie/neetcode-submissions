class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_len = len(nums) + 1
        count = dict()
        freq = freq = [[] for _ in range(max_len)]

        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1
        
        for value in count:
            reps = count[value]
            freq[reps].append(value)

        final = []
        tracker = 0
        for index in range(max_len - 1, -1, -1):
            if freq[index] == []:
                continue
            else:
                for i in freq[index]:
                    if tracker == k:
                        break
                    final.append(i)
                    tracker += 1
        
        return final

        


