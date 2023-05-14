def find_sum_indexes(list_num, target_sum):
    result = []

    def backtrack(start, current_sum, index_list):
        if current_sum == target_sum:
            result.append(''.join(map(str, index_list)))
            return

        if current_sum > target_sum or start >= len(list_num):
            return

        for i in range(start, len(list_num)):
            new_sum = current_sum + list_num[i]
            new_index_list = index_list + [i]

            backtrack(i + 1, new_sum, new_index_list)

    backtrack(0, 0, [])
    return result

list_num = [3, 5, 3, 4, 6, 7, 1, 2, 5]
target_sum = 8

indexes = find_sum_indexes(list_num, target_sum)
print(indexes)