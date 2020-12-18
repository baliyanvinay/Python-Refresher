from abc import ABC, abstractmethod
class A(ABC):
    @classmethod
    @abstractmethod
    def m1(self):
        print('In class A, method m1')

    @abstractmethod
    def m3(self):
        print('In class A, method m3')

class B(A):
    @classmethod
    def m1(self):
        print('In class B, method m1')

    def m3(self):
        print('In class B, method m3')

class C(B):
    def m4(self):
        print('In class C, method m4')


c=C()
c.m3()
c.m4()