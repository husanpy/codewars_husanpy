"""https://www.codewars.com/kata/52b7ed099cdc285c300001cd
   Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, 
   and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.
   First I get a new list that combines all continuing intervals into one, then I get sum of new intervals"""


def covered_segments(segments: list):
    segments.sort(key=lambda x: x[0])
    ints = [*segments]

    i = 1
    while i < len(ints):
        a, b = ints[i - 1]
        x, y = ints[i]
        if a <= x < b:
            if y <= b:
                del ints[i]
                continue
            else:
                ints[i - 1] = (a, y)
                del ints[i]
                continue
        i += 1
    return ints


def sum_of_intervals(intervals: list):
    ints = covered_segments(intervals)
    count = 0
    for el in ints:
        count += el[1] - el[0]
    return count


def main():
    print(sum_of_intervals([(1, 5)]))
    print(sum_of_intervals([(1, 5), (1, 5)]))
    print(sum_of_intervals([(1, 5), (6, 10)]))
    print(sum_of_intervals([(1, 4), (3, 5), (7, 10)]))


if __name__ == '__main__':
    main()
