import sys
import copy

# redirection to file-input from standard-input.
sys.stdin = open("input.txt", 'r')

# see data format in 'input.txt'
nm = input().split()
n = int(nm[0])
m = int(nm[1])
c = list(map(int, input().rstrip().split()))

VALUE = n
NUM_COIN = m
COIN = c

# list of making change using coins
price = [1] + [0] * VALUE

# iterate coins we have.
for coin in COIN:
    # 
    for i in range(coin, n+1):
        price[i] = price[i] + price[i - coin]

# VALUE ways using coins
print(price[VALUE+1])
