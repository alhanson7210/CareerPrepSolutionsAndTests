brute_force: bool = False
semi_efficient: bool = False
most_efficient_solution: bool = True

def median(a: int, b: int) -> int:
    return int((a+b)/2)

def merge_sort(a_seq: list, b_seq: list) -> list:
    a_i = 0
    a_l = len(a_seq)
    b_i = 0
    b_l = len(b_seq)
    ordered_list = list()
    while a_i != a_l or b_i != b_l:
        if a_i == a_l:
            ordered_list.extend(b_seq[b_i:])
            break
        if b_i == b_l:
            ordered_list.extend(a_seq[a_i:])
            break
        if a_seq[a_i] < b_seq[b_i]:
            ordered_list.append(a_seq[a_i])
            a_i += 1
        else:
            ordered_list.append(b_seq[b_i])
            b_i += 1
    return ordered_list

def sorted_array_median(a_seq: list, b_seq: list, n: int) -> int:
    ordered_list = merge_sort(a_seq, b_seq)
    if n % 2 != 0:
        mid = n // 2
        return ordered_list[mid]
    else:
        m_l = n // 2
        m_r = m_l - 1
        mvl = ordered_list[m_l]
        mvr = ordered_list[m_r]
        return median(mvl, mvr)

def modified_merge_sort(a_seq: list, b_seq: list, n: int) -> list:
    limit = n // 2 + 1
    ai = 0
    al = len(a_seq)
    bi = 0
    bl = len(b_seq)
    half_ordered_list = list()
    while (ai != al or bi != bl) and ai + bi != limit:
        if ai == al:
            half_ordered_list.append(b_seq[bi])
            bi += 1
            continue
        if bi == bl:
            half_ordered_list.append(a_seq[ai])
            ai += 1
            continue
        if a_seq[ai] < b_seq[bi]:
            half_ordered_list.append(a_seq[ai])
            ai += 1
        else:
            half_ordered_list.append(b_seq[bi])
            bi += 1
    return half_ordered_list

def half_sorted_array_median(a_seq: list, b_seq: list, n: int) -> int:
    half_ordered_list = modified_merge_sort(a_seq, b_seq, n)
    if n % 2 == 0:
        return median(half_ordered_list[-2], half_ordered_list[-1])
    else:
        return half_ordered_list[-1]

def solution_one(a_seq: list, b_seq: list, n: int) -> int:
    return sorted_array_median(a_seq, b_seq, n)

def solution_two(a_seq: list, b_seq: list, n: int) -> int:
    return half_sorted_array_median(a_seq, b_seq, n)

def two_array_median(a_seq: list, b_seq: list, n: int) -> int:
    if brute_force:     # Big(o) = N
        return solution_one(a_seq, b_seq, n)
    elif semi_efficient:    # Big(o) = N/2 => N
        return solution_two(a_seq, b_seq, n)
    elif most_efficient_solution:
        return solution_two(a_seq, b_seq, n)

def main() -> None:
    a = [1, 3, 5, 9, 11]
    b = [2, 4, 8, 10]
    n = len(a) + len(b)
    o_mdn = two_array_median(a, b, n)
    print("Median of odd array is {}".format(o_mdn))
    a.remove(11)
    n -= 1
    e_mdn = two_array_median(a, b, n)
    print("Median of even array is {}".format(e_mdn))

if __name__ == "__main__":
    main()

