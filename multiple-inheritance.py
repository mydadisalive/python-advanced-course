class ClassA:
    def method_A(self):
        print("Method A from ClassA")

class ClassB:
    def method_B(self):
        print("Method B from ClassB")

class ClassC(ClassA, ClassB):
    def __init__(self):
        super(ClassA, self).__init__()  # Call constructor of ClassA
        super(ClassB, self).__init__()  # Call constructor of ClassB
        print("Constructor of ClassC")

    def method_C(self):
        print("Method C from ClassC")

# Create an instance of ClassC
obj = ClassC()

# Access methods from ClassA and ClassB
obj.method_A()
obj.method_B()

# Access the method from ClassC
obj.method_C()
