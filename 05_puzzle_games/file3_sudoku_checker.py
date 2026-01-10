def is_valid(row):
    nums = [n for n in row if n != 0]
    return len(nums) == len(set(nums))

grid = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8]
]

for row in grid:
    print("Valid Row:", is_valid(row))
