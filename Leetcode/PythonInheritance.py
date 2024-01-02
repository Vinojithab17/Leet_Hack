class A:
    def method(self):
        print("Method in class A")

class B(A):
    def method(self):
        print("Method in class B")


class C(A):
    def method(self):
        print("Method in class C")


class D(C,B):
    pass

# Creating an instance of class D
d_instance = D()

# Calling the method
d_instance.method()
