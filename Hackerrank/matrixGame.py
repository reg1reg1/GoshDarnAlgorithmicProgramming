#Skeleton code for upcoming adversary

#assuming x is a 2d array of integers
def sample2(x):
  op1=0
  op2=0
  cols=[]
  colNum=len(x[0])
  choices=[]
  
  for i in range(colNum):
    bl=[row[i] for row in x]
    cols.append(max(bl))
    #print(bl)
  cols.sort(reverse=True)
  turn =0
  print(cols)
  for i in range(colNum):
    if(turn%2)==0:
      op1+=cols.pop(0)
      print(op1)
    else:
      op2+=cols.pop(0)
      print(op2)
    turn+=1
  return op1-op2


def main():
  #declaring a 2d array in the only way I know of size 
  #n is no of rows
  #m is no of columns

  n=5
  m=7
  inp=[
    [1,2,3,4],
    [2,3,4,5],
    [5,4,3,2],
    [2,4,5,6],
    [1,2,11,2]
  ]
  print(sample2(inp))

if __name__ == '__main__':
  main()