from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 입력 문자열이 비어있는 경우 빈 문자열 반환
        if not t or not s:
            return ""
        
        # t의 각 문자에 대한 카운트를 저장하는 딕셔너리 생성
        dict_t = Counter(t)
        # 필요한 고유 문자의 수 (t 내의 고유 문자 수)
        required = len(dict_t)
        
        # 슬라이딩 윈도우의 시작과 끝 포인터
        l, r = 0, 0
        # 현재 윈도우에 t의 모든 고유 문자가 적절한 횟수로 포함되어 있는지 추적
        formed = 0
        # 현재 윈도우 내의 각 문자의 카운트
        window_counts = Counter()
        
        # 결과를 저장할 변수: (윈도우 길이, 시작 인덱스, 끝 인덱스)
        ans = float("inf"), None, None
        
        # 오른쪽 포인터를 문자열의 끝까지 이동
        while r < len(s):
            character = s[r]
            # 현재 문자가 t에 포함되어 있다면 카운트 업데이트
            if character in dict_t:
                window_counts[character] += 1
                
                # 현재 문자의 카운트가 t 내의 카운트와 일치하면 formed 증가
                if window_counts[character] == dict_t[character]:
                    formed += 1
            
            # 모든 고유 문자가 윈도우 내에 적절히 포함되어 있으면,
            # 윈도우의 시작 포인터를 이동하여 가능한 가장 짧은 윈도우 탐색
            while l <= r and formed == required:
                character = s[l]
                
                # 현재 윈도우가 지금까지 찾은 것 중 최소 길이라면 결과 업데이트
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                # 윈도우에서 문자를 제거하며 윈도우 크기 조정
                if character in dict_t:
                    window_counts[character] -= 1
                    if window_counts[character] < dict_t[character]:
                        formed -= 1
                
                # 왼쪽 포인터 이동
                l += 1
            
            # 오른쪽 포인터 이동
            r += 1
        
        # 결과 반환 (조건을 만족하는 윈도우가 없으면 빈 문자열 반환)
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

# 테스트 실행 예
solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print(solution.minWindow(s, t))  # "BANC" 출력 예상
