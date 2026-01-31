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
    def __init__(self, stream_id: str, budget: int) -> None:
        self.stream_id = stream_id
        self.budget = budget
        self.transactions = dict()
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        for action, _, cost in data_batch:
            if action == "buy":
                self.budget += cost
            elif action == "sell":
                self.budget -= cost
        return "critical_error: insufficent funds for all transactions" \
            if self.budget < 0 else "sufficent funds for all transactions"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return f"critical: surpassed the budget by {self.budget}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        valid_data = list()
        for data in data_batch:
            if isinstance(data, tuple) and len(data) == 3:
                action, item, _ = data
                if not criteria or item == criteria and \
                        action in ["buy", "sell"]:
                    valid_data.append(data)
        return valid_data


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        print("Initializing Event Stream...")
        self.stream_id = stream_id
        self.error = 0
        self.events = 0
        print(f"Stream ID: {stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        for data in data_batch:
            if "error" in data:
                self.error += 1
            self.events += 1
        return f"Event analysis: {self.error} \
error detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        valid_data = list()
        for data in data_batch:
            if isinstance(data, str):
                if not criteria or criteria in data:
                    valid_data.append(data)
        return valid_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"total events": self.events,
                "total errors": self.error}


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def get_stream(self, stream_id: str) -> Optional[DataStream]:
        for stream in self.streams:
            if stream.stream_id == stream_id:
                return stream

    def proccess_data(self, stream_id: str,  data_batch: List[Any],
                      criteria: Optional[str]) -> None:
        stream = self.get_stream(stream_id)
        if not stream:
            print("Warning: invalid stream id")
            return
        valid_data = stream.filter_data(data_batch, criteria)
        print(f"proccessing data: {valid_data}")
        process_output = stream.process_batch(valid_data)
        stats = stream.get_stats()
        print(process_output)
        print(", ".join([f"{key}: {value}" for key, value in stats.items()]))


def main() -> None:
    event_input: List[Any] = [
                                "event: user_login",
                                "critical_error: database connection lost",
                                "alert: user_logout",
                                "error: high memory usage",
                                404,
                                None
                            ]
    event_stream = EventStream("EVENT001")
    transaction_stream = TransactionStream
    steam_processor = StreamProcessor()
    steam_processor.add_stream(event_stream)
    steam_processor.proccess_data("EVENT001", event_input, "error")



if __name__ == "__main__":
    main()
