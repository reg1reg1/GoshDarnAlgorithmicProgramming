from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        que = deque()
        que.append(beginWord)
        level = 1
        while que:
            size = len(que)
            for i in range(size):
                word = que.popleft()
                word_list = list(word)
                for i in range(len(word_list)):
                    orig = word_list[i]
                    for c in range(ord('a'), ord('z')+1):
                        if word_list[i] == chr(c): continue
                        word_list[i] = chr(c)
                        trans_word = "".join(word_list)
                        if trans_word == endWord:
                            return level+1
                        if trans_word in wordSet:
                            que.append(trans_word)
                            wordSet.remove(trans_word)
                    
                    word_list[i] = orig
            level += 1
        return 0