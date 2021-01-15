def transpose_arr(pre_list):
    n = len(pre_list)
    transport = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transport[i].append(pre_list[j][i])
    return transport


def list_triplets(pre_list):
    """returns lists of 3x3 elements"""
    result = []
    start, end = 0, 3
    for i in range(0, len(pre_list), 3):
        for _ in range(3):
            result.append(pre_list[i][start:end] + pre_list[i + 1][start:end] + pre_list[i + 2][start:end])
            start += 3
            end += 3
        start, end = 0, 3
    return result


def row_validator(*lists):
    for list_r in lists:
        if len(list_r) != 9:
            return False
        for el in list_r:
            if 0 in el:
                return False
            if len(el) != 9:
                return False
            if sum(el) != 45:
                return False
            if len(set(el)) != 9:
                return False
            for cell in el:
                if cell > 9 or cell < 1:
                    return False
    return True


def valid_solution(board):
    transport_lc = transpose_arr(board)
    thirds = list_triplets(board)
    return row_validator(board, transport_lc, thirds)


def main():
    print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]]))


if __name__ == '__main__':
    main()
