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
            return
        elif msg is not None and restart is False:
            end = time.time()
            runtime = end - self.runtime
            self.runtime = end
            print(f'{msg}: {runtime}')
            return
        else:
            end = time.time()
            print(f'Benchmark No.{self.benchmark_counter}: {(end - self.runtime)}')
            return


with measure_performance() as p:
    time.sleep(1)
    p.benchmark('1st step')

    time.sleep(2)
    p.benchmark('2nd step', restart=True)

    time.sleep(3)
    p.benchmark()
