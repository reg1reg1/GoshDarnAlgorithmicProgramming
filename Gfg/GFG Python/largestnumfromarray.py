# Python3 Program to get the maximum 
# possible integer from given array 
# of integers... 
  
  
# custom comparator to sort according 
# to the ab, ba as mentioned in description 
def comparator(a, b): 
    ab = str(a) + str(b) 
    ba = str(b) + str(a) 
    return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 
      
def myCompare(mycmp): 
      
    # Convert a cmp= function into a key= function 
    class K(object): 
        def __init__(self, obj, *args): 
            self.obj = obj 
        def __lt__(self, other): 
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other): 
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other): 
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other): 
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other): 
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other): 
            return mycmp(self.obj, other.obj) != 0
    return K 
# driver code 
if __name__ == "__main__": 
    
    sorted_array = sorted(a, key=myCompare(comparator)) 
    number = "".join([str(i) for i in sorted_array]) 
    print(number) 