import pandas as pd
import random

df = pd.read_csv("lotto.csv")
result = []

while len(result) < 10:
    # 1~45까지 랜덤한 숫자 6개를 생성하여 target_numbers 리스트에 저장
    target_numbers = random.sample(range(1, 46), 6)

    # 각 행과 target_numbers와의 중복 개수 계산
    df['match'] = df.apply(lambda row: len(set(row) & set(target_numbers)), axis=1)

    # match 열의 값이 3 이상인 행만 추출하여 개수 세기
    match_count = (df['match'] >= 3).sum()

    # match 열의 값이 3 이상인 행의 개수가 20~25 사이일 때 target_numbers 리스트 추가
    # if match_count >= 24 and match_count <= 28:
    #     result.append(sorted(target_numbers))

    if match_count <= 15:
        result.append(sorted(target_numbers))

# 결과 출력
for r in result:
    print(r)
