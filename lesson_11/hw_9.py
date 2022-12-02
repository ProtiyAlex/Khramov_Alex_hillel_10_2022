from queue import Queue
from threading import Thread

START = 100
END = 20000
QTY_THREAD = 5


def get_primes(start: int, end: int, qe: Queue):
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            qe.put(number)


def main():
    queue = Queue()

    interval = [i for i in range(START, END + 1, (END - START) // QTY_THREAD)][:-1] + [
        END
    ]
    thread = [
        Thread(
            target=get_primes,
            args=(
                interval[i],
                interval[i + 1],
                queue,
            ),
        )
        for i, _ in enumerate(interval[:-1])
    ]
    _ = [i.run() for i in thread]

    result = []
    while not queue.empty():
        result.append(queue.get())

    return sorted(result)


if __name__ == "__main__":
    print(main())
