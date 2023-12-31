#0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 
#먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 
#그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 
#합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
#26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 
#8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
#위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
#N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

import sys

# readline을 사용하여 입력값을 읽어옴
s = sys.stdin.readline().rstrip()

  # 입력값을 보존하기 위해 원래의 값을 저장
result = 0
count = 0
if int(s) < 10: # 주어진 수가 10보다 작다면 0을 붙여 두 자리 수로 만든다.
        s = '0' + s
origin = s
while True:
    # 각 자리 숫자를 더한다.
    total = int(s[0]) + int(s[1])
    # 새로운 수를 만든다.
    s = s[1] + str(total % 10) #total에 두자리 수가 들어가면 한자리 수로 바꿔서 s에 넣어준다.
    count += 1
    # 처음 입력값과 같아지면 반복문 종료
    if s == origin:
        break

# write를 사용하여 출력값을 출력
sys.stdout.write(str(count) + '\n')
