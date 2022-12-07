#https://leetcode.com/problems/determine-if-two-strings-are-close/
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cletW1=[0]*26
        cletW2=[0]*26
        if len(word1)!=len(word2):
            return false
        set1=set()
        set2=set()
        for i in word1:
            cletW1[ord(i)-97]+=1
            set1().add(i)
        for i in word2:
            cletW2[ord(i)-97]+=1
            set2().add(i)
        
        return cletW1.sort()==cletW2.sort() and set1==set2