class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Lớp Student kế thừa lớp Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # Gọi hàm khởi tạo của lớp cha (Person)
        super().__init__(name, age)
        self.student_id = student_id  # Thuộc tính riêng của Student

    # Ghi đè phương thức __str__ để in thông tin chi tiết hơn
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}"

# Ví dụ sử dụng
if __name__ == "__main__":
    # Tạo đối tượng thuộc lớp Person
    a = Person("Noname", 20)
    a.setName("Huynh hoc")
    
    # Tạo đối tượng thuộc lớp Student
    b = Student("Anonymous", 21, "S12345")
    
    print(a)  # In đối tượng Person
    print(b)  # In đối tượng Student

    
