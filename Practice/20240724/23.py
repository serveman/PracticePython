import time

def longtime_job(num):
    print('job start %d' % num)
    time.sleep(0.5)
    return ('job done %d' % num)

print('=' * 20)
print('일반적인 방식으로 생성한 함수의 결과값 리턴')
list_job_by_normal = [longtime_job(i) for i in range(5)]
for _ in list_job_by_normal:
    print('생성 후 결과값 출력: ', _)

print('=' * 20)
print('Generator를 이용하여 생성한 함수의 결과값 리턴')
list_job_by_generator = (longtime_job(i) for i in range(5))
for _ in list_job_by_generator:
    print('생성 후 결과값 출력: ', _)
