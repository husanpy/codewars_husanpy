"""this function finds next bigger number by creating permutations and sorting them into a list, then returning element next to argument
   but when it comes to large numbers it's not effective"""

def next_bigger(n):
    num = str(n)
    listOfNums = set([int(''.join(nums)) for nums in itertools.permutations(num, len(num))])
    listOfNums = sorted(list(listOfNums))
    if listOfNums.index(n) == len(listOfNums) - 1:
        return -1
    return listOfNums[listOfNums.index(n) + 1]
