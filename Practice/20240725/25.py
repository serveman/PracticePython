# regex: https://wikidocs.net/4308
# \d - 숫자와 매치된다. [0-9]와 동일한 표현식이다.
# \D - 숫자가 아닌 것과 매치된다. [^0-9]와 동일한 표현식이다.
# \s - 화이트스페이스(whitespace) 문자와 매치된다. [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈칸은 공백 문자(space)를 의미한다.
# \S - 화이트스페이스 문자가 아닌 것과 매치된다. [^ \t\n\r\f\v]와 동일한 표현식이다.
# \w - 문자+숫자(alphanumeric)와 매치된다. [a-zA-Z0-9_]와 동일한 표현식이다.
# \W - 문자+숫자(alphanumeric)가 아닌 문자와 매치된다. [^a-zA-Z0-9_]와 동일한 표현식이다.

# 유용한 단축키 - CDW
# Ctrl + ` (백틱): 터미널창으로 커서 이동
# Alt + 클릭          : 멀티라인 개별 선택
# Alt + Shift + 드래그: 멀티라인 연속 선택
# Ctrl + Alt + 방향키 : 멀티라인 연속 선택
# Ctrl + D               : 현재 단어 선택
# Ctrl + Shift + L       : 선택한 단어와 동일한 단어 모두 선택
# Alt + Shift + 좌우방향키: 선택영역 확장 / 축소
# (영역 선택하지 않은 상태) Alt + Shift + 상하방향키: 현재 라인 복제

import re

def sample_regex_with_match(inputPattern, inputString):
    p = re.compile(inputPattern)
    m = p.match(inputString)
    if m:
        print(f'Match found: "{m.group()} in string "{inputString}" with pattern: "{inputPattern}"')
    else:
        print(f'No matched in string "{inputString}" with pattern: "{inputPattern}"')

sample_regex_with_match('[a-z]+', 'python')
print('-' * 20)
sample_regex_with_match('[a-z]+', '3 python')
