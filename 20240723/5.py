# 리터럴, 와일드카드
menu = int(input('메뉴를 입력해주세요> '))

match menu:
    case 1:     print('커피')
    case 2:     print('에이드')
    case 3:     print('우유')
    case _:     print('1~3만 입력 가능!')

print('=' * 40)

# 시퀀스, OR, 캡쳐
examples = [
    ['apple'],
    ['홍길동', '이순신'],
    [1],
    [2],
    ['1', '2'],
    ['1'],
    ['2'],
    ['3'],
    ['4'],
    ['a', 'b', 'c'],
    ['a', 'b'],
    ['score', 95, 82, 77]
]

for x in examples:
    print('input: ', x, end='\t')
    match x:
        case ['apple']:             print('시퀀스 1')
        case ['홍길동', '이순신']:   print('시퀀스 2')
        case ['1'] | ['2']:         print('OR 1')
        case ['3' | '4']:           print('OR 2')
        case [1 | 2]:               print('OR 3')
        case ['a', z]:              print('캡쳐 1: ', z)
        case ['a', y, z]:           print('캡쳐 2: ', y, z)
        case ['score', *z]:         print('캡쳐 3: ', *z)
        case _:                     print('해당없음')

