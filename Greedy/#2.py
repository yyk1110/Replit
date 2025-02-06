print("Version 2")
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

count = (M // (K+1)) * K #가장 큰 수가 더해질 횟수
count += M % (K+1)

result = 0
result += (count) * first #가장 큰 수 * 반복 가능한 수
result += (M - count) * second #두 번째로 큰 수 더함

print(result)



'''
print('Version.1')
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
'''