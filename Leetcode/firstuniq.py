class Solution:
    def firstUniqChar(self, s: str) -> int:
        cmap=[0]*26
        l = len(s)
        b= False
        ch = 0
        for i in range(l):
            cmap[ord(s[i])-97]+=1

        for i in range(l):
            if cmap[ord(s[i])-97]==1:
                b= True
                ch = i
                break

        if b:
            return i
        return -1
def main():
    str1="leetcode"
    s= Solution()
    print(s.firstUniqChar(str1))



if __name__ == '__main__':
    main()