def phone(key):
    telecom = {'011': 'SKT', '016': 'KT', '019': 'LGU'}.get(key, "알수없음")
    return telecom

firstNumber = input("Input Phone Number: ").split('-')[0]
print(phone(firstNumber))
