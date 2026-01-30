from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class StreamError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        valid_data = list()
        for data in data_batch:
            if isinstance(data, str) and criteria and criteria in data:
                valid_data.append(data)
        return valid_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        ...


class SensorStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class TransactionStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: int) -> None:
        print("Initializing Event Stream...")
        self.stream_id = stream_id
        self.error = 0
        self.events = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Stream ID: {self.stream_id}, Type: System Events")
        print(f"Processing event batch: {data_batch}")
        valid_data = self.filter_data(data_batch, "status")
        print(f"Event analysis: {self.events} events, {self.error} \
errors detected")
        return "\n".join([f"{data[0]}: {data[1]}" for data in valid_data])

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        valid_data = list()
        for data in data_batch:
            if isinstance(data, tuple) and len(data) == 2\
                    and all(isinstance(x, str) for x in data):
                if not criteria or criteria in data[1]:
                    self.error += 1 if "error" in data[0] else 0
                    self.events += 1
                    valid_data.append(data)
        return valid_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = dict()
        stats["events"] = self.events
        stats["error"] = self.error
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def get_stream(self, stream_id: int) -> Optional[DataStream]:
        for stream in self.streams:
            if stream.stream_id == stream_id:
                return stream

    def process_data(self, stream_id: int, data_batch: List[Any]) -> None:
        stream: Any = None
        for x in self.streams:
            if x.stream_id == stream_id:
                stream = x
        if stream:
            result = stream.process_batch(data_batch)
            print("")
        else:
            raise StreamError("invalid stream id")


def main() -> None:
    event_steam = EventStream(0)
    steam_processor = StreamProcessor()
    steam_processor.add_stream(event_steam)


if __name__ == "__main__":
    main()
