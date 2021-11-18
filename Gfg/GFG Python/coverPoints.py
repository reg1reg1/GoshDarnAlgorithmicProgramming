

def coverPoints(X,Y):
	curr_dist=0
	num = len(X)

	for i in range (0,num-1):
		curr_dist+=max(abs(X[i]-X[i+1]),abs(Y[i]-Y[i+1]))
	return curr_dist


X = [3,5]
Y= [-5,-3]
print(coverPoints(X,Y))

