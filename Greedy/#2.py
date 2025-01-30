N, M, K = map(int, input().split())
data = list(map(int, input().split()))
result = 0

data.sort() #입력받은 수 정렬
first = data[N-1]
second = data[N-2]

while True:
  for i in range(K): #가장 큰 수 K번 더하기
    if M == 0:
      break
    result += first
    M -= 1 #더할 때마다 1 빼기
  if M == 0:
    break
  result += second
  M -= 1

print(result)