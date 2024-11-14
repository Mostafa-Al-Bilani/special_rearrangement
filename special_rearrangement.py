"""a function that rearranges a list so that all even numbers appear before all odd numbers"""
nums = [1,2,4,5,7,9,6]
LENGTH = len(nums)
def special_rearrangement(nums):
    new_list = []
    odd_list = []
    for i in range(LENGTH):

        if nums[i] % 2 == 0:
            new_list.append(nums[i])

        if nums[i] % 2 != 0:
            odd_list.append(nums[i])

    new_list.extend(odd_list)
    return new_list
print(special_rearrangement(nums))
