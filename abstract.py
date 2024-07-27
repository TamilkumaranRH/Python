""" from abc import ABC,abstractmethod
class college(ABC):
    def college_info(self):
        print("Welcome back")
    @abstractmethod
    def fees(self):
        pass

class college1(college):
    def fees(self):
        print("20,000")
    def course(self):
        print("BSC")
s=college1()
s.college_info()
s.fees()
s.course() """


from abc import ABC,abstractmethod
class college(ABC):
    def college_info(self):
        print("Welcome back")
    @abstractmethod
    def fees(self):
        pass

class college1(college):
    def course(self):
        print("BSC(cs)")
class college2(college1):
    def fees(self):
        print("20,000")
s=college2()
s.college_info()
s.fees()
s.course()