n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin # 해당 화페로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

# 이것이 취업을 위한 코딩 테스트다 with 파이썬, 나동빈 저서 참고