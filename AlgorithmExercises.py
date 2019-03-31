import math

def num_ways(n):
    if (n==0) or n==1:
        return 1
    else:
        return num_ways(n-1)+num_ways(n-2)


def num_way_bottom_up(n):
    if n==0 or n==1
        return 1
    else:
        nums = n+1
        nums[0] = 1
        nums[1] = 1
        for i in range(2,n):
            nums[i] = nums[i-1]+nums[i-2]
    return nums[n]

def num_way_bottom_up2 (n, x):
    if n in x:
        return 1
    else:
        return sum([num_way_bottom_up2(n-i)for i in x if n>=0])

def num_way_bottom_up2_1(n,x):
    if n in x:
        return 1
    else:
        nums = n+1
        nums[0] = 1
        nums[1] = 1
        for i in range(len(x),n):
            if n>=0:
                nums[i] = sum([nums[n-j] for j in x])
    return nums[n]


# given a set of coordinate points = [(-2, 4), (0,-2), ...], find the closet two
def destince(point):
    # x = sqrt(x^2 + y^2)
    return ()