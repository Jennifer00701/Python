''' 출력 : 나이는 31살이다. '''

year = int(input())
age_type = input()

if age_type == 'korea':
        answer = year-2000+1
        print(f'2030년에 2000년생의 한국식 나이는 {answer}살이다.')

elif age_type == 'year':
        answer = year-1999
        print(f'2030년에 1999년생의 연 나이는 {answer} 살이다.')

'''
1. year = input을 int로 받겠다.
        * 2030
2. age_type = age_type이 korea or year 와 동일 == 하다면? answer 출력
        * year(2030) + 1 = 2031 / year(2030) - 2000 = 31
3. f스트링을 이용해 2023년에 나이는 ~ {answer} 이다. 출력 
'''




''' -------------원래 문제 코드---------------

year = int(input())
age_type = input()

if age_type == :
        answer = 

elif age_type == :

print()

'''