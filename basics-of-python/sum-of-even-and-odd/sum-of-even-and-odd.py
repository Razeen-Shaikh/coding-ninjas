nums = input()
even_sum = 0
odd_sum = 0

for num in nums:
    if int(num) % 2 == 0:
        even_sum += int(num)
    else: odd_sum += int(num)

print(even_sum, odd_sum)
