class Solution:
    def print_n_times(self, value: str, times: int) -> None:
        def recursion(value: str, times: int) -> None:
            print(f"{times}. {value}")
            if times == 1:
                return
            recursion(value, times - 1)
        recursion(value, times)