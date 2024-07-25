# decorator.py
import time

def elapsed(original_func):     # 기존 함수를 인수로 받음
    def wrapper():
        start = time.time()
        result = original_func()    # 기존 함수 수행
        end = time.time()

        print("함수 수행시간: %f 초" %(end - start))       # 기존 함수의 수행시간 출력
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수를 실행합니다.")


# decorated_myfunc = elapsed(myfunc)    # @elapsed 데코레이터로 인해 더 이상 필요없다
# decorated_myfunc()

myfunc()
