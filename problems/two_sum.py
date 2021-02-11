class Solution:
    @staticmethod
    def two_sum(nums: list, target: int) -> list:
        checked_values = dict()
        for idx, value in enumerate(nums):
            if value not in checked_values:
                checked_values[value] = [idx]
            else:
                checked_values[value].append(idx)

        for key in checked_values.keys():
            delta = target - key
            if delta in checked_values:
                if key == delta:
                    if len(checked_values[key]) != 2:
                        continue
                    return checked_values[key]
                else:
                    key_idx = checked_values[key][0]
                    delta_idx = checked_values[delta][0]
                    return [key_idx, delta_idx]

def main() -> None:
  manual_test_list = [2,7,13,11]
  actual = Solution.two_sum(manual_test_list, 9)
  expected = [0,1]
  print("for list: {}, actual: {}, expected {}".format(manual_test_list, actual,expected))
  manual_test_list = [3,2,5,11]
  actual = Solution.two_sum(manual_test_list, 7)
  expected = [1,2]
  print("for list: {}, actual: {}, expected {}".format(manual_test_list, actual,expected))
  manual_test_list = [3,3,1,5]
  actual = Solution.two_sum(manual_test_list, 6)
  expected = [0,1]
  print("for list: {}, actual: {}, expected {}".format(manual_test_list, actual,expected))

if __name__ == "__main__":
    main()

