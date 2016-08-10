class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.shortestMap = {}
        for w1 in words:
            for w2 in words:
                if w1 != w2:
                    key = (w1, w2) if w1 < w2 else (w2, w1)
                    if key in self.shortestMap:
                        pass
                    else:
                        distance = self.findShortest(words, w1, w2)
                        self.shortestMap[key] = distance


    def findShortest(self, words, word1, word2):
        choice = -1
        index = 0
        for w in words:
            if w == word1:
                choice = 0
                break
            elif w == word2:
                choice = 1
                break
            index += 1

        min_distance = len(words)
        base = index
        index += 1
        for w in words[index:]:
            #print base, index, choice, w, word1, word2
            if choice == 0 and w == word2:
                distance = index - base
                if distance < min_distance:
                    min_distance = distance
                base = index
                choice = 1
            elif choice == 0 and w == word1:
                base = index
            elif choice == 1 and w == word1:
                distance = index - base
                if distance < min_distance:
                    min_distance = distance
                base = index
                choice = 0
            elif choice == 1 and w == word2:
                base = index
            index += 1

        return min_distance

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        key = (word1, word2) if word1 < word2 else (word2, word1)
        return self.shortestMap[key]



# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        choice = -1
        index = 0
        for w in words:
            if w == word1:
                choice = 0
                break
            elif w == word2:
                choice = 1
                break
            index += 1

        min_distance = len(words)
        base = index
        index += 1
        for w in words[index:]:
            print base, index, choice, w, word1, word2
            if choice == 0 and w == word2:
                distance = index - base
                if distance < min_distance:
                    min_distance = distance
                base = index
                choice = 1
            elif choice == 0 and w == word1:
                base = index
            elif choice == 1 and w == word1:
                distance = index - base
                if distance < min_distance:
                    min_distance = distance
                base = index
                choice = 0
            elif choice == 1 and w == word2:
                base = index
            index += 1

        return min_distance

s = Solution()
words = ["this","is","a","long","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","run","running","rainy"]
word1 = "this"
word2 = "sentence"
print s.shortestDistance(words, word1, word2)

ws = WordDistance(words)
for w1 in words:
    for w2 in words:
        if w1 != w2:
            print ws.shortest(w1, w2)
