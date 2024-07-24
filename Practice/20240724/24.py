import re

data = '''
park 800905-1049118
kim  700905-1059119
'''

pat = re.compile('(\d{6}[-][1234]{1})\d{6}')
print(pat.sub('\g<1>******', data))
