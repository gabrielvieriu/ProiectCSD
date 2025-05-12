import time
import tracemalloc
import subprocess

def calculate_file_hash(file_path):
    cmd = ['openssl', 'dgst', '-sha256', '-hex', file_path]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True)
    output = result.stdout.strip()
    hash_value = output.split('=')[-1].strip()
    return hash_value


def measure_performance(function, *args, **kwargs):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = function(*args, **kwargs)
    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    execution_time = end_time - start_time
    memory_usage = peak / 1024

    return result, execution_time, memory_usage
