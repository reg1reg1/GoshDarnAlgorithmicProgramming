'''
Given an array print subarray with sum atleast k

'''
def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        countdef=-1
        sumdef=0
        start=0
        fin=start
        while start< len(k):
            if (sumdef<k):
                fin=fin+1
                sumdef=sumdef+A[fin]
            elif sumdef>k:
                start=start+1
                sumdef=sumdef-A[start]
            if(sumdef==k):
                countdef=1
                break
        if(countdef==-1):
            print(-1)
        else:
            print(fin-start+1)
