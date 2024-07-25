class SimpleClass:
    def __datacamp(self):
        return 'datacamp'

    def call_datacamp(self):
        return self.__datacamp()
    
obj = SimpleClass()
print(obj.call_datacamp())
print(obj._SimpleClass__datacamp())     # 메소드 이름이 mangle 됨
