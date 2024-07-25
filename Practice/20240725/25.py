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

import re, time

class sample_regex:
    def __init__(self):
        pass

    def _time_check(func):
        def wrapper(*args):
            start = time.time()
            func(*args)
            end = time.time()
            print(f'running time: %.6f' %(end-start))
            print('-' * 20)
        return wrapper

    @_time_check
    def __call__(self, inputPattern, inputString, inputOption):
        self.inputPattern = inputPattern
        self.inputString = inputString
        self.inputOption = inputOption
        self._processing()

    def _processing(self):
        self._match_option()
        self._print_option()

    def _match_option(self):
        p = re.compile(self.inputPattern)
        match self.inputOption:
            case 'search': 
                self.m = p.search(self.inputString)
            case 'findall':
                self.m = p.findall(self.inputString)
            case 'finditer':
                self.m = p.finditer(self.inputString)
            case _:
                self.m = p.match(self.inputString)

    def _print_option(self):
        if self.m:
            match self.inputOption:
                case 'search' | 'match': 
                    result = f'start: {self.m.start()} to end: {self.m.end()}, text: {self.m.group()}'
                case 'findall':
                    result = '\n' + '\n'.join([f'text: {g}' for g in self.m]) + '\n'
                case 'finditer':
                    result = '\n' + '\n'.join([f'start: {g.start()} to end: {g.end()}, text: {g.group()}' for g in self.m]) + '\n'
                case _:
                    result = 'not exist option'
                
            print(f'{self.inputOption}: "{result}" in string "{self.inputString}" with pattern: "{self.inputPattern}"')
        else:
            print(f'Nothing {self.inputOption} in string "{self.inputString}" with pattern: "{self.inputPattern}"')

sr = sample_regex()
sr('[a-z]+', 'python', 'match')
sr('[a-z]+', '3 python', 'match')
sr('[a-z]+', '3 python', 'search')
sr('[a-z]+', 'life is too short', 'search')
sr('[a-z]+', 'life is too short', 'findall')
sr('[a-z]+', 'life is too short', 'finditer')
