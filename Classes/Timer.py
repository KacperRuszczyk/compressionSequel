import time

class Timer:
    def measure(self,fun,method,File_Path):
        start = time.perf_counter()
        fun(method,File_Path)
        end = time.perf_counter()
        return end - start