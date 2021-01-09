"""this function finds next bigger number by creating permutations and sorting them into a list, then returning element next to argument
   but when it comes to large numbers it's not effective"""

def next_bigger(n):
    num = str(n)
    listOfNums = set([int(''.join(nums)) for nums in itertools.permutations(num, len(num))])
    listOfNums = sorted(list(listOfNums))
    if listOfNums.index(n) == len(listOfNums) - 1:
        return -1
    return listOfNums[listOfNums.index(n) + 1]


#the one below proved to be right, tho I don't know the beneath algorithm. I found it at https://codereview.stackexchange.com/questions/115609/next-bigger-number-with-the-same-digits
#and it was saying:
"""
1. Find largest index i such that array[i − 1] < array[i].
2. Find largest index j such that j ≥ i and array[j] > array[i − 1].
3. Swap array[j] and array[i − 1].
4. Reverse the suffix starting at array[i].
"""
#the original link tho: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
#I slightly modified the code to match the test requirements (I didn't change algorithm, just converted str, int, list and etc. And implemented managing of raised errors
def next_bigger(n):
    array = list(map(int, str(n)))
    try:
        i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
        j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
        array[j], array[i - 1] = array[i - 1], array[j]
        array[i:] = reversed(array[i:])
        return int(''.join([str(i) for i in array]))
    except ValueError:
        return -1
