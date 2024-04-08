''' 출력 : 12 or 2
'''

start = int(input()) # 첫 달 저축 금액 입력
before = int(input()) # 두 번째 달 부터 70만원 모일 때까지 저축 금액 입력

money = start
month = 1
total = start + before

while money < 70:
    money += before
    month += 1

    if total <= 100: #total이 100보다 작거나 같으면
        print(f'100만원을 모으기까지 걸린 개월수는 {month}달 입니다.')

    elif total > 100 and total <= 200: # total이 100보다 크고 200보다 작거나 같으면
        print(f'100만원 이상을 모으기까지 걸린 개월수는 {month}달 입니다.')
        
    else total > 200: # 위 모든 조건이 거짓이면
    print(f'200만원 이상을 모으기까지 걸린 개월수는 {month}입니다.')

'''
2를 출력 시 

1. start 에 첫 금액 입력 (10입력)
2. while(반복문)_befor에 사용할 금액 입력(90) = money += before < 10+90 =100 > 총 2달 소요 

'''


''' -------------원래 문제 코드---------------
start = int(input())
before = int(input())
after = int(input())

money = start
month = 1

while money < 70:
    money += 
    month += 1

while < 100:
    month += 1

print(month)


첫 달에 저축하는 금액을 나타내는 정수 start
두 번째 달 부터 70만 원 이상 모일 때까지 매월 저축하는 금액을 나타내는 정수 before
100만 원 이상 모일 때 까지 매월 저축하는 금액을 나타내는 정수 after

100만 원 이상을 모을 때까지 걸리는 개월 수를 출력하도록 빈칸을 채워 코드를 완성해 주세요.

30 + 70
'''