n = int(input())
m = int (input())
st = 1
while True:
    print(st, end='')
    st = 1+(st+m-2)%n
    if st == 1:
        break
print()