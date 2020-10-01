#Given an array of integers, find if the array contains any duplicates.

#Your function should return true if any value appears at least twice in the array, 
#     and it should return false if every element is distinct.

def main():
    nums = [1,2,3,4] # false
    test(False,containsDuplicates(nums), nums)

    nums = [] # false
    test(False,containsDuplicates(nums), nums)
    
    nums = [1] # false
    test(False,containsDuplicates(nums), nums)

    nums = [2,2,5,4,1] # true - start at beginning
    test(True,containsDuplicates(nums), nums)

    nums = [1,2,3,1] # true - not adjacent
    test(True,containsDuplicates(nums), nums)

    nums = [1,2,3,3] # true - at the end
    test(True,containsDuplicates(nums), nums)


def containsDuplicates(nums):
    # option 1 ->  O(n)
    """ -> use a hash table?? """ 
    hash_table = dict()
    for x in nums:
        if x in hash_table.keys():
            return True
        hash_table.update({x : 1})
    return False       

    # option 2 -> O(n log n)
    """ nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False """

    # option 3 -> O(n)
    """ if len(nums) == len(set(nums)):
        return False
    elif len(nums) > len(set(nums)):
        return True """


def test(first, second, nums):
    if first == second:
        print("actual:", first, "| getting:", second, "=> Pass <=", nums)
    else:
        print("actual:", first, "| getting:",  second, "=> Fail <=", nums)

if __name__ == "__main__":
    main()