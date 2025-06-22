#Q: Given that the two integers in an array, when added up, give the answer target and output in the form of indices


def twosum(nums,target):
  num_map{}#hash map

  for i, num in enumerate(nums):
    complement=target-num
    if complement in num_map:
      return [num_map[complement],i]
    num_map[num]=i

nums=[2,11,15,7]
target=9
result=twosum(nums,target)
print(result)
