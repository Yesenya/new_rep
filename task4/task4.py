a = input('введите путь к файлу')
nums = open(a, 'rb').read().decode('utf-8')
print(b)

# nums = [2,3,4]
# nums = map(int, input())
sum = 0
step = 0
for num in nums:
    sum+= num
avg_num_r = round(sum/ len(nums))
for num in nums:
    while num != avg_num_r:
        if num > avg_num_r:
            num -= 1
            step += 1
        elif num < avg_num_r:
            num += 1
            step +=1
print(step)


