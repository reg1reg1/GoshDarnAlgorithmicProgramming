
from typing import List
def solve(listObj)->List:
    wordSet = set()
    ans = []

    for word in listObj:
        if ''.join(sorted(word)) not in wordSet:
            ans.append(word)
            wordSet.add(''.join(sorted(word)))

    return sorted(ans)

def main():
	wordList=["code","car","arc","fly","edoc"]
	print(solve(wordList))

if __name__ == '__main__':
	main()