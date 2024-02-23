# 한 줄에 하나씩 숫자 입력받기 (정수로 출력이라 a+b+c = 6이 나옴 )
'''
a = int(input('a 입력'))
b = int(input('b 입력'))
c = int(input('c 입력'))
print(a,b,c,a+b+c)
'''

# 한 줄에 여러 개의 숫자 입력받기 ( 한 줄에 입력 하되, 공백을 사이에 두고 입력해라 (int값이라 동일하게 + 처리 = 18))
# split -> 문자열을 자르는 메서드 
'''a,b,c = map(int,input('a b c 값 입력').split())
print(a,b,c,a+b+c) '''

# 문자1.split(문자2) : 문자 2를 기준으로 문자 1을 자른다.
    # print (text) 우리가 입력한 것 2024.02.02 그대로 출력
    # text를 .split하겠다 ('.') 점 기준으로 문자열을 자른다. y,m,d 에 각 각 담기 2024 02 02 잘린 문자열 출력
''' 
text = input ('날짜 입력 yyyy.mm.dd')
y,m,d = text.split('.')
print(text,y,m,d) '''

# map 함수, 집합형태 - 리스트, 튜플, 등등 
# 집합형태로 a,b,c 를 한번에 int로 묶어준 것 
'''a,b,c = map(int,['1','2','3'])
print(a,b,c,a+b+c)'''

# 총 정리 아래 주석 된 전체 코드를 한 줄로 출력 완성
a,b,c = map (int,input('a b c 값 입력').split())
print(a,b,c,a+b+c)
''' 
text = input ('a b c 값 입력')
text = text.split()
a,b,c = map(int,text)'''




