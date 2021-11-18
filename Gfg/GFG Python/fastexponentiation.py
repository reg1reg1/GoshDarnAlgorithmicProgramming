def fastexp(x,y):
	temp=1
	while(y>0):

		if(y%2!=0):
			temp=temp*x


		y=y/2
		x=x*x
	return x
print fastexp(2,7)


