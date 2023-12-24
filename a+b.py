# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 
# 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
import sys
result = []
T = input()
for i in range(0,int(T)):
    test_case = sys.stdin.readline().strip().split(' ') #입력한 두 숫자를 공백을 기준으로 나눠서 리스트에 저장
    result.append(int(test_case[0]) + int(test_case[1])) #두 수를 더한 값을 result에 넣어줌
for j in range(0,len(result)):
    sys.stdout.write(str(result[j]) + '\n') #A+B를 한줄씩 출력
