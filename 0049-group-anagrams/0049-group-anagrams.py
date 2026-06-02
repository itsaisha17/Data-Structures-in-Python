from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # store every anagaram group
        groups = defaultdict(list)

        #looping strs->word->ch
        for word in strs:
            freq = [0] * 26  #freq array--> as if freq same then they anagram

            for ch in word:
                freq[ord(ch) - ord("a")] += 1  #ord('a')= 97...its the ascii value


            groups[tuple(freq)].append(word) #same freq wale in same buckets

        return list(groups.values()) #return groups

#Neetcode says-> Sorting mat karo, Direct character counts store karo