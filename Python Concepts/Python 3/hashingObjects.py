
# Check this out: https://docs.python.org/3/reference/datamodel.html#object.__eq__



class Student:
	def __init__(self,name,grade,age,_id):
		self.name = name
		self.grade = grade
		self.age = age
		self._id = _id
	def __repr__(self):
		return repr((self.name, self.grade, self.age))
	def weighted_grade(self):
		return 'CBA'.index(self.grade) / float(self.age)

	#I have overridden equals,therefore I must define hashcode or it will be implicitly set to None
	def __eq__(self,other):
		if self._id==other._id:
			return True

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

	for x in student_objects:
		db.add(x)

	
	
if __name__ == '__main__':
	main()