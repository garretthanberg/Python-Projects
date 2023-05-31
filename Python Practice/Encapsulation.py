class Course():
    def __init__(self):
        self.course = 'Python Programming Course'
        self._studentName = 'Lucas'
        self.__teacherName = 'Paul' # This is an example of protected encapsulation.

    def getTeacherName(self):
        print(self.__teacherName) # This is an example of private encapsulation.

    def setTeacherName(self, teacher):
        self.__teacherName = teacher

obj = Course() # This object will make us of the protected/private encapsulation.
obj._studentName = 'Garrett'
print(obj._studentName)
obj.getTeacherName()
obj.setTeacherName('Dan')
obj.getTeacherName()

