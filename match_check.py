# 선택한 숫자 6개 중 기존의 행의 숫자와 몇 개가 중복되는 확인하는 코드, 중요!!!!
import pandas as pd
df = pd.read_csv("lotto.csv")

target_numbers = [3,6,22,23,24,38]

# 각 행과 target_numbers와의 중복 개수 계산
df['match'] = df.apply(lambda row: len(set(row) & set(target_numbers)), axis=1)

# match 열의 값이 3 이상인 행만 추출
result = df[df['match'] >= 3]

# 결과 확인
print(result)

result = df['match'].value_counts()
print(result)
# x이름의 열을 기준으로 내림차순
# sorted_data = result.sort_values(by='match', ascending=False)
# print(sorted_data)
