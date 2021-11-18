#chiru@oath.com
def fuzzyMatch(inp,pattern):
	k = len(pattern)
	i=0
	j=0
	while i<len(inp):
		if j<k and inp[i]==pattern[j]:
			#print("Match at ",i," char ",inp[i])
			i=i+1
			j=j+1
		else:
			i=i+1
	if j==k:
		return True
	return False


def main():
	inp="The cat is in the hat"
	a1=["cah","cabt","The cat is th","tt","isth","catb","act","cat is hat","cahat"]
#expected output as per my understanding
	#True,False,True,True,True,False,False,True

#Is catb considered a fuzzy match? I think no, but I could have understood the question wrong

#If pattern is of higher length than input?
	#I do not understand then what the program should print
	#One case would be to ignore the characters and match only till inpstring length
	#The other could be to reiterate from the beginning over the new string
#	if inp was cat, and pattern was catcatcat, would it be a fuzzy match?

#Swapping characters does not count has a fuzzy match as per my understanding
	#if it does, then my algorithm will fail (might have to use a variation of Levenshtein Distance)

	for i in a1:
		print(fuzzyMatch(inp,i))

if __name__ == '__main__':
	main()