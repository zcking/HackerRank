# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())

nums = set(sorted(list(map(int, raw_input().split()))))
nums.remove(max(nums))
print max(nums)

   