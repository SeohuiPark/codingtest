
import sys

n,k= map(int,sys.stdin.readline().split())

cnt = 0
coin_list = []
for _ in range(int(n)):
    num = int(sys.stdin.readline())
    if num > int(k):
        break
    else:
        coin_list.append(num)

for _ in range(len(coin_list)):
    if k >0:
        coin = coin_list.pop()
        cc = (k // coin)
        if cc >0:
            k = k - (k//coin)*coin
            cnt += cc
        else:
            pass
    else:
        break

print(cnt)