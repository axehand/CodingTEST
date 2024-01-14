# 연도가 주어졌을 때, 윤년이면 1, 
# 아니면 0을 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서,
# 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# 예를 들어, 2012년은 4의 배수이면서 100의 배수가 아니라서 윤년이다. 
# 1900년은 100의 배수이고 400의 배수는 아니기 때문에 윤년이 아니다. 
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.
# import sys

# year = int(sys.stdin.readline().strip())

# if int(year % 4) == 0: #4의 배수일때
#     if int(year % 100) != 0:# 100의 배수가 아니면 윤년
#         sys.stdout.write('1')
#     elif int(year % 400) == 0:# 400의 배수면 윤년
#         sys.stdout.write('1')
#     else:
#         sys.stdout.write('0')
# else:
#     sys.stdout.write('0')

# def solution(a, b):
#     answer = 0
#     if a % 2 != 0 and b  % 2 != 0: #두 수가 전부 홀수인지 판별
#         answer = (a*a) + (b*b)
#     elif a % 2 != 0 or b  % 2 != 0: #두 수중 한가지 수가 홀수인지 판별 
#         answer =  2 * (a + b)      
#     else:                          #둘 다 짝수일 경우 
#         if a-b < 0:                 #결과값이 음수가 되는경우
#             answer = -(a - b)       #값을 양수로 변환
#         else:
#             answer = a-b            #음수가 아닐경우 a-b의 값을 대입
#     return answer

# ========================================================================== 1330 두 수 비교하기
# a, b = map(int, input().split())

# if a == b:
#     print("==")
# else:
#     if a < b:
#         print('<')
#     elif a > b: 
#         print('>')

# ========================================================================== 9498 시험 성적
# score = int(input())
# if score >= 0 and score <= 100:
#     if score >= 90:
#         print("A")
#     elif score >= 80:
#         print("B")
#     elif score >= 70:
#         print("C")
#     elif score >= 60:
#         print("D")
#     else:
#         print("F")
# else:
#     print("점수가 올바르지 않습니다.")

# ========================================================================== 14681 사분면 고르기
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print(1)
# else:
#     if x < 0 and y > 0:
#         print(2)
#     elif x < 0 and y < 0:
#         print(3)
#     else:
#         print(4)
# ==========================================================================
h,m = map(int,input().strip().split(' '))
answer_h = 0
answer_m = 0
answer_m = m - 45
if answer_m < 0:
    answer_m += 60
    h -= 1
    if h < 0:
        answer_h = 23
print(answer_h , answer_m)