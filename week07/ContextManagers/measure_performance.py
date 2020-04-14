import time


class measure_performance:
    def __init__(self):
        self.start = time.time()
        self.runtime = time.time()
        self.benchmark_counter = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print(f'Finished for: {time.time() - self.start}')

    def benchmark(self, msg=None, restart=False):
        self.benchmark_counter += 1
        if msg is not None and restart is True:
            end = time.time()
            runtime = end - self.start
            self.runtime = end
            print(f'{msg}: {runtime}')

        elif msg is not None and restart is False:
            end = time.time()
            runtime = end - self.runtime
            self.runtime = end
            print(f'{msg}: {runtime}')

        else:
            end = time.time()
            print(f'Benchmark No.{self.benchmark_counter}: {(end - self.runtime)}')
