def hammingDistance(w1, w2):
    return sum(map(lambda (c1, c2) : int(c1 != c2), zip(w1, w2)))

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        self.hops = {}
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                w1 = wordList[i]
                w2 = wordList[j]

                dist = hammingDistance(w1, w2)
                if dist == 1:
                    if w1 not in self.hops:
                        self.hops[w1] = set([w2])
                    else:
                        self.hops[w1].add(w2)

                    if w2 not in self.hops:
                        self.hops[w2] = set([w1])
                    else:
                        self.hops[w2].add(w1)

        visited = set()
        stack = [(beginWord, 0, [beginWord])]
        distances = []

        #print self.hops

        if beginWord not in self.hops:
            for h in self.hops.keys():
                dist = hammingDistance(beginWord, h)
                if dist == 1:
                    self.hops[beginWord] = set([h])
                    self.hops[h].add(beginWord)
        if endWord not in self.hops:
            for h in self.hops.keys():
                dist = hammingDistance(endWord, h)
                if dist == 1:
                    self.hops[endWord] = set([h])
                    self.hops[h].add(endWord)

        while len(stack) > 0:
            curr, dist, path = stack.pop(0)
            #print curr, dist
            if curr == endWord:
                distances.append((dist, path))
                continue
            elif curr not in visited:
                visited.add(curr)
                if curr in self.hops:
                    for hop in self.hops[curr]:
                        copy = path[:]
                        copy.append(hop)
                        stack.insert(0, (hop, dist + 1, copy))

        return min(distances) if len(distances) > 0 else 0


wordList = ["hot","dog"] #,"dog","lot","log"] #,"hit","cog"]
begin = "hot"
end = "dog"

s = Solution()
print s.ladderLength(begin, end, wordList)
                
