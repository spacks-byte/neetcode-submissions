class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = []
        currentAnagrams = {}
        for i, word in enumerate(strs):
            wordInOrder = ''.join(sorted(word))
            if wordInOrder in currentAnagrams:
                index = currentAnagrams[wordInOrder]
                final[index].append(word)
            else:
                currentAnagrams[wordInOrder] = len(final)
                final.append([word])
        return final



        