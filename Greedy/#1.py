n = 1260
count = 0

coin_types = [500, 100, 50, 10] #큰 단위 화폐부터 선언

for coin in coin_types:
  count += n // coin #해당 화폐로 거슬러 줄 수 있는 동전 개수
  n %= coin #거슬러 준 후 잔액

print(count)