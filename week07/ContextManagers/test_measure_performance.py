import unittest
from measure_performance import measure_performance
import time


class TestMeasurementPerformance(unittest.TestCase):
    def test_measurement_performance_with_one_benchmark_only_with_message(self):
        with measure_performance() as p:
            time.sleep(1)
            p.benchmark('1st step')

    def test_measurement_performance_with_benchmarks_with_message_and_true_restart(self):
        with measure_performance() as p:
            time.sleep(1)
            p.benchmark('1st step')

            time.sleep(4)
            p.benchmark('2nd step', restart=True)

    def test_measurement_performance_with_more_benchmark(self):
        with measure_performance() as p:
            time.sleep(1)
            p.benchmark('1st step')

            time.sleep(2)
            p.benchmark('2nd step', restart=True)

            time.sleep(3)
            p.benchmark()


if __name__ == '__main__':
    unittest.main()
