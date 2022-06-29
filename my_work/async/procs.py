
from multiprocessing import cpu_count
from queue import SimpleQueue
from time import perf_counter
from unittest import result
import sys
from primes import is_prime, NUMBERS


def main() -> None:
    if len(sys.argv) < 2:
        workers = cpu_count()
    else:
        workers = int(sys.argv[1])
    print(f'Checking{len(NUMBERS)} numbers with {workers} processes:')

    jobs:JobQueue = SimpleQueue()
    results:ResultQueue = SimpleQueue()
    t0 = perf_counter()

    for n in NUMBERS:
        jobs.put(n)

    for _ in range(workers):
        proc = Process(target=worker,args=(jpbs,results))
        proc.start()
        jobs.put(0)
    while True:
        n,prime,elapsed = results.get()
        label = 'P' if prime else ''
        print(f'{n:16}{label}{elapsed:9.6f}s')
        if jobs.empty():
            break
    elapsed = perf_counter() - t0
    print(f'Total time: {elapsed:.2f}s')

if __name__ == '__main__':
    main()