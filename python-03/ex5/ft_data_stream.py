import time
from typing import Generator


def proccess_event(event_list: list) -> Generator:
    count = 0
    for event in event_list:
        if event.__class__.__name__ != "tuple" or len(event) != 3:
            yield "invalid event"
            continue
        name, level, action = event
        count += 1
        yield f"Event {count}: Player {name} (level {level}) {action}"


def next_prime(count: int) -> Generator:
    num = 2
    ret = ""
    if count.__class__.__name__ != "int":
        print("not a number")
        return
    while count:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
        if prime:
            count -= 1
            ret = str(num)
            if count != 0:
                ret += ", "
            yield ret
        num += 1


def fib_seq(limit: int) -> Generator:
    count = 0
    previous = 0
    current = 1
    res = 0
    ret = ""
    if limit.__class__.__name__ != "int":
        print("not a number")
        return
    while count < limit:
        if limit <= 0:
            return
        if count == 0:
            ret = str(previous)
            if count != limit - 1:
                ret += ", "
            yield ret
        elif count == 1:
            ret = str(current)
            if count != limit - 1:
                ret += ", "
            yield ret
        else:
            res = current + previous
            previous = current
            current = res
            ret = str(res)
            if count != limit - 1:
                ret += ", "
            yield ret
        count += 1


def stream_analyze(event_list: list) -> None:
    print("\n=== Stream Analytics ===\n")
    events = iter((event_list))
    count = 0
    hight_level = 0
    treasure_count = 0
    level_up_count = 0
    for event in events:
        if event.__class__.__name__ != "tuple":
            print("invalid event")
            continue
        _, level, event = event
        if level.__class__.__name__ != "int" or\
                event.__class__.__name__ != "str":
            print("invalid event")
            continue
        count += 1
        if level > 10:
            hight_level += 1
        if "level" in event:
            level_up_count += 1
        elif "found" in event:
            treasure_count += 1
    print(f"Total events processed: {count}")
    print(f"High-level players (10+): {hight_level}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")


def calculate_mem_usage(current: float) -> None:
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {(time.time() - current):.5f} seconds")


def main() -> None:
    current = time.time()
    event_list = [("Paul", 49, "item_found "),
                  ("Paul", 50, "level_up "),
                  ("Henry", 51, "item_found "),
                  ("Bob", 53, "death "),
                  ("Liam", 54, "quest_complete "),
                  ("Charlie", 70, "death "),
                  ("Frank", 71, "death "),
                  ("Frank", 72, "item_found "),
                  ("Eve", 73, "quest_complete "),
                  ("Diana", 74, "kill "),
                  ("Grace", 109, "item_found ")]

    print("=== Game Data Stream Processor ===")
    event_count = len(event_list)
    try:
        print(f"\nProcessing {event_count} game events...\n")
        proccessed_events = proccess_event(event_list)
    except (ValueError, IndexError, TypeError):
        print("Invalid input")
        exit(1)
    for _ in range(event_count):
        print(next(proccessed_events))
    stream_analyze(event_list)
    calculate_mem_usage(current)
    fib_count = 9
    print("\n=== Generator Demonstration ===")
    print(f"Fibonacci sequence (first {fib_count}): ", end="")
    fib = fib_seq(fib_count)
    for num in fib:
        print(num, end="")
    print("")
    prime_count = 9
    print(f"Prime numbers (first {prime_count}): ", end="")
    prime = next_prime(prime_count)
    for num in prime:
        print(num, end="")


if __name__ == "__main__":
    try:
        main()
    except TypeError:
        print("you need to pass the correct prameters to the program")
