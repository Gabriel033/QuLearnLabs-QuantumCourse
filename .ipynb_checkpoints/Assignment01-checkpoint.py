def avg_three(input: list[int]) -> float:
    sum = 0
    count = 0
    for val in input:
        if(val%3 == 0):
            sum += val
            count += 1
    return sum / count if count != 0 else 0

inp: list[int] = [1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33]
output = avg_three(inp)
print(output)