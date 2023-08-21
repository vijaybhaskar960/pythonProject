class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    @property
    def msg(self):
        return self.name+" got Grade "+self.grade
    @msg.setter
    def msg(self, msg):
        sent = msg.split(" ")
        print(sent)
        self.name = sent[0]
        self.grade = sent[-1]

s = Student("Vaishu",'A++')
#s.setter("Vaishu got a grade A")
s.msg = 'Vaishu got a grade A'
print(s.grade)
print(s.name)
print(s.msg)


class Student1:
    def __init__(self, marks):
        self.marks = marks

    def per(self):
        return (self.marks/600)*100
    @property
    def marks(self):
        return self.__marks
    @marks.setter
    def marks(self, value):
        self.__marks = value


t = Student1(400)
t.marks = 500
print(t.marks)
print(t.per(), "%")


class Student2:
    def __init__(self, marks):
        self.marks = marks

    def per(self):
        return (self.marks/600)*100

    def getter(self):
        return self.__marks

    def setter(self, value):
        self.__marks = value

    marks = property(getter, setter)


m = Student2(400)
m.marks = 300
print(m.marks)
print(m.per(), "%")
