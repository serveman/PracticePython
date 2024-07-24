_SimpleClass__name = 'data_camp'    # 변수 선언을 먼저 한다

class SimpleClass:
    def return_name(self):
        return __name
    
obj = SimpleClass()
print(obj.return_name())        # 이렇게 해도 출력이 된다?!