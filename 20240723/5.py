# 리터럴, 와일드카드
menu = int(input('메뉴를 입력해주세요> '))

match menu:
    case 1:     print('커피')
    case 2:     print('에이드')
    case 3:     print('우유')
    case _:     print('1~3만 입력 가능!')

print('=' *20)

# 시퀀스, OR, 캡쳐
examples = [
    ['apple'],
    ['홍길동', '이순신'],
    ['1'],
    ['a', 'b'],
    ['score', 95, 82, 77]
]

for x in examples:
    match x:
        case ['apple']:             print('시퀀스\t', x)
        case ['홍길동', '이순신']:   print('시퀀스\t', x)
        case ['1'] | ['2']:         print('OR\t', x)
        case ['a', z]:              print('캡쳐\t', z)
        case ['score', *z]:         print('캡쳐\t', z)

