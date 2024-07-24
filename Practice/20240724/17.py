class Sample():
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
    
obj1 = Sample()
print(' \n'.join(dir(obj1)))


class SecondSample(Sample):
    def __init__(self):
        super().__init__()
        self.a = 'overridden'
        self._b = 'overridden'
        self.__c = 'overridden'

obj2 = SecondSample()
print(' \n'.join(dir(obj2)))
print('SecondSample.a = \t\t%10s' % obj2.a)     # Sample 클래스를 상속 받았다
print('SecondSample._b = \t\t%10s' % obj2._b)
print('SecondSample._Sample__c = \t%10s' % obj2._Sample__c)
print('SecondSample._SecondSample__c = %10s' % obj2._SecondSample__c)
print('SecondSample.__c = %10s' % obj2.__c)     # 실제 SecondSample 클래스에는 __c를 정의하지 않았다. 상속만 받았을 뿐
