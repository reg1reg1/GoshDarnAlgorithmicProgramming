import os
import sys

'''
Python 2.x Default input type converted
Python 3.x Not type converted, taken as string
'''

def main():
  t = int(input().strip())
  for i in range(t):
    num = input().strip()
    fin = len(num)
    fflag=False
    for i in range(fin-2,-1,-1):
      if num[i]<num[i+1]:
        fflag=True
        k=i
        break
    if fflag is True:
      j = k+1
      for i in range(fin-1,k,-1):
        if num[i]>num[k]:
          j=i
          break
    
      tlist=list(num)
      tlist[k], tlist[j] = tlist[j], tlist[k]
      cstr = ''.join(tlist)
      pre = cstr[:k+1]
      post = ''.join(sorted(cstr[k+1:]))
      ans = pre + post
      print(ans)
    else:
      print("not possible")

if __name__ == '__main__':
  main()



