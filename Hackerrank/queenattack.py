def queensAttack(N, k, r_q, c_q, obstacles):
	
	nearSameRowLeftDist=r_q-1
	nearSameRowRightDist=N-r_q
		

	nearSameColumnUpDist=c_q-1
	nearSameColumnDownDist=N-c_q
		
	nearLowerLeftDiagDist=min(N-r_q,c_q-1)
	nearUpperRightDiagDist=min(r_q-1,N-c_q)

	nearUpperLeftDiagDist=min(r_q-1,c_q-1)
	nearLowerRightDiagDist=min(N-r_q,N-c_q)
	
	ans=0
	if k!=0:
		for i in range(len(obstacles)):
			rowObst= obstacles[i][0]
			colObst= obstacles[i][1]
			if rowObst==r_q:
				if colObst<c_q:
					nearSameRowLeftDist=min(nearSameRowLeftDist,abs(colObst-c_q)-1)
				else:
					nearSameRowRightDist=min(nearSameRowRightDist,abs(colObst-c_q)-1)
			elif colObst==c_q:
				if rowObst<r_q:
					nearSameColumnUpDist=min(nearSameColumnUpDist,abs(rowObst-r_q)-1)
				else:
					nearSameColumnDownDist=min(nearSameColumnDownDist,abs(rowObst-r_q)-1)
			elif abs(r_q-rowObst)==abs(c_q-colObst):
				if (rowObst>r_q and colObst<c_q):
					nearLowerLeftDiagDist=min(nearLowerLeftDiagDist,abs(rowObst-r_q)-1)
				elif (rowObst<r_q and colObst>c_q):
					nearUpperRightDiagDist=min(nearUpperRightDiagDist,abs(rowObst-r_q)-1)
				elif (rowObst<r_q and colObst<c_q):
					nearUpperLeftDiagDist=min(nearUpperLeftDiagDist,abs(rowObst-r_q)-1)
				else:
					nearLowerRightDiagDist=min(nearLowerRightDiagDist,abs(rowObst-r_q)-1)
	ans= ans+nearSameColumnDownDist+nearSameColumnUpDist

	ans=ans+nearSameRowLeftDist+nearSameRowRightDist

	ans=ans+nearLowerLeftDiagDist+nearUpperRightDiagDist

	ans=ans+nearUpperLeftDiagDist+nearLowerRightDiagDist

	return ans




def main():
	n=5
	r_q=4
	c_q=3
	obstacles=[[5,5],[4,2],[2,3]]
	print(queensAttack(5,3,r_q,c_q,obstacles))

if __name__ == '__main__':
	main()
