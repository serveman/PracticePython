import time

# 곱셈 연산 속도 측정
start_time = time.time()
for i in range(1000000):
    result = i * i
end_time = time.time()
time_multiplication = end_time - start_time

# 제곱 연산 속도 측정
start_time = time.time()
for i in range(1000000):
    result = i ** 2
end_time = time.time()
time_exponentiation = end_time - start_time

print('i*i  = %f' % time_multiplication)
print('i**2 = %f' % time_exponentiation)
