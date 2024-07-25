class SimpleClass:
    def __init__(self):
        self.__datacamp = "Excellent"
    
    def get_datacamp(self):
        return self.__datacamp
    
obj = SimpleClass()
print(obj.get_datacamp())
print(obj.__datacamp)       # 예외 발생
