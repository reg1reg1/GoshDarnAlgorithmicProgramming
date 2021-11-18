def longest_flat(array):
    i=1
    c=1
    ans=1
    elem =array[0]
    while i<len(array):
        #print(array[i],elem,c)
        if array[i]==elem:
            c+=1
        else:
            ans=max(ans,c)
            elem=array[i]
        i+=1
    ans=max(ans,c)
    return ans

def main():
    x=[1,1,1]
    y=[1,2,3,3,3,2]
    print(longest_flat(x))

if __name__ == '__main__':
    main()
