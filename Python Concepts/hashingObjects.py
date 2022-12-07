
# Check this out: https://docs.python.org/3/reference/datamodel.html#object.__eq__



class Student:
	def __init__(self,name,grade,age,_id):
		self.name = name
		self.grade = grade
		self.age = age
		self._id = _id
	# __repr__() function returns the object representation in string format. The repr() function returns the string representation of the value passed to eval function by default. For the custom class object, it returns a string enclosed in angle brackets that contains the name and address of the object by default.
	def __repr__(self):
		return repr((self._id,self.name, self.grade, self.age))
	def weighted_grade(self):
		return 'CBA'.index(self.grade) / float(self.age)

	#I have overridden equals,therefore I must define hashcode or it will be implicitly set to None
	#equals identify the position in the bucket of hashmap
	def __eq__(self,other):
		if self._id==other._id:
			return True
    #identifies the bucket in the hashmap
	def __hash__(self):
		return hash(self._id)

	def __ne__(self, other):
		return not(self == other)




db = set()



def main():
	student_objects = [
		Student('john', 'A', 15,"123"),
        Student('jane', 'B', 12,"321"),
        Student('dave', 'B', 10,"3214"),
        Student('Albert','A',12,"ac32fe"),
        Student('Albert','B',22,"dasdsa"),
        Student('Albert','C',24,"dsadsada"),
        Student('Albert','D',24,"dakalda")
	]
	#Adding to a set
	for x in student_objects:
		db.add(x)
	for x in db:
		print(x)
	#this element won't get added as the key already exists (__hash__ value is same)
	db.add(Student('Not Albert','F',24,'dakalda'))

	for x in db:
		print(x)
	#sort by grade alone	
	ranking_student = sorted(student_objects,key=lambda x:x.grade)
	print(ranking_student)


	#sort by grade, then age (tie-breaker in case grade is same)
	ranking_again = sorted(student_objects, key = lambda x: (x.grade, x.age))
	print(ranking_again)
if __name__ == '__main__':
	main()