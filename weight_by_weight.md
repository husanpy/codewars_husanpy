# How to sort list (or _string_) both lexicographically and by second parameter

Doing regular tasks on [codewars](https://www.codewars.com/) I suddenly encountered a task which looks really simple, but is interesting in realization.

First let's start from the task's description.


## Weight for weight

My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example `99` will have "weight" `18`, `100` will have "weight" `1` so in the list `100` will come before `99`. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

## Example

`"56 65 74 100 99 68 86 180 90"` ordered by numbers weights becomes: `"100 180 90 56 65 74 68 86 99"`.

When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers: `100` is before `180` because its "weight" (1) is less than the one of `180` (9) and 180 is before `90` since, having the same "weight" (9), it comes before as a _string_.

All numbers in the list are positive numbers and the list can be empty.

## Notes
* it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
* Don't modify the input
* For C: The result is freed.

___
## So interesting part for me was: 
> When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers

Because previously I didn't know how to sort lists by two keys in the same time. With lexicographic sorting it turned out to be pretty easy: you first sort the list lexicographically and then by second key.

And below is my solution in Python and it worked out:
```python
def order_weight(strng):
    lst = strng.split()
    lst.sort()
    lst.sort(key=lambda x: sum(map(int, x)))
    return ' '.join(lst)


def main():
    print(order_weight(input()))


if __name__ == '__main__':
    main()
```

And this is another solution with different realization of the abovementioned approach:
```python
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
```
