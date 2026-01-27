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


def stream_analize(event_list: list) -> None:
    print("\n=== Stream Analytics ===\n")
    events = iter((event_list))
    count = 0
    hight_level = 0
    treasure_count = 0
    level_up_count = 0
    for event in events:
        if event.__class__.__name__ != "tuple" or len(event) != 3:
            continue
        _, level, event = event
        if not isinstance(level, int) or not isinstance(event, str):
            continue
        count += 1
        if level > 10:
            hight_level += 1
        " Total events processed: 1000 High-level players (10+): 342 Treasure events: 89 Level-up events: 156 "


def main():
    event_list = [("alice", 5, "killed monster"),
                  ("bob", 12, "found treasure"),
                  ("charlie", 8, "leveled up")]
    print("=== Game Data Stream Processor ===")
    event_count = len(event_list)
    print(f"\nProcessing {event_count} game events...\n")
    proccessed_events = proccess_event(event_list)
    for _ in range(event_count):
        print(next(proccessed_events))


if __name__ == "__main__":
    main()
