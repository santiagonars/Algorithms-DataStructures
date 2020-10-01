# Given an array, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    """for i in range(k):
        a = nums.pop()
        nums.insert(0, a)
    return nums """
    if k > 0 and k <= len(nums):
        nums[:] = nums[-k:] + nums[:len(nums)-k]
        return nums
    elif k > len(nums):
        k = k - len(nums)
        nums[:] = nums[-k:] + nums[:len(nums)-k]
    else:
        return nums

    return nums

def main():
    nums = [1,2,3,4,5,6,7]
    k = 11
    # print(rotate(nums, k))

    test([5,6,7,1,2,3,4], rotate([1,2,3,4,5,6,7], 3))
    test([2,34,4,77,-53,100], rotate([100,2,34,4,77,-53], 5))
    test([4,5,6,7,1,2,3], rotate([1,2,3,4,5,6,7], 11))


def test(first, second):
    if first == second:
        print("actual:", first, "getting", second, "=> Pass")
    else:
        print("actual:", first, "getting",  second, "=> Fail")


if __name__ == '__main__':  
    main()