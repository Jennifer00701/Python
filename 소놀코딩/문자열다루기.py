# 문자열 인덱스 (공백 포함됨)
# 양수 = 0부터 시작 
# 음수 = - n 번 부터 시작 ~ -1 로 종료 
'''
text = 'abc'
print(text[0])
print(text[1])
print(text[2])
'''

# 문자열 슬라이스 - 어디서부터 어디까지 문자열을 빼온다.
text = 'abc de fg'
print (text [0:6])
print (text [-5:-1]) # 음수는 마지막 -1 전 까지 출력 
print(text[5:])