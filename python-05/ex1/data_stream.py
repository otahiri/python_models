from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod
import sys


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
        return {"process": 0}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.type = "humidity"
        self.average = {"temp": [0, 0], "humidity": [0, 0], "pressure": [0, 0]}
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        for sensor, value in data_batch:
            if sensor in self.average.keys():
                self.average[sensor][0] += 1
                self.average[sensor][1] += value
        try:
            res = f"avg {self.type}: \
{self.average[self.type][1] / self.average[self.type][0]}"
        except ZeroDivisionError:
            res = f"avg {self.type}: 0"
        return res

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        valid_data = []
        self.type = criteria
        for sense, value in data_batch:
            if sense in ["temp", "humidity", "pressure"] and value >= 0:
                if not criteria or criteria == sense:
                    valid_data.append([sense, value])
        return valid_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        res = dict()
        for key in self.average.keys():
            try:
                res[key] = self.average[key][1] / self.average[key][0]
            except ZeroDivisionError:
                pass
        return res


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, budget: int) -> None:
        self.stream_id = stream_id
        self.budget = budget
        self.transactions: Dict[str, Union[str, int, float]] =\
            {"buy": 0, "sell": 0}
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        for action, cost, _ in data_batch:
            if action == "buy":
                self.budget -= cost
                self.transactions["buy"] += cost
            elif action == "sell":
                self.budget += cost
                self.transactions["sell"] += cost
        return "critical_error: insufficent funds for all transactions" \
            if self.budget < 0 else "sufficent funds for all transactions"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return self.transactions

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        valid_data = list()
        min_price = 0
        try:
            min_price = int(criteria) if criteria else 0
        except (ValueError):
            print("Warning: invlaid criteria")
        for data in data_batch:
            try:
                _, cost, _ = data
                if not criteria or cost > min_price:
                    valid_data.append(data)
            except (ValueError, TypeError):
                pass
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
        valid_data = list()
        if not stream:
            print("Warning: invalid stream id")
            return
        try:
            valid_data = stream.filter_data(data_batch, criteria)
        except (KeyError, ValueError, TypeError):
            print("Error: invalid data", file=sys.stderr)
        print(f"proccessing data: {valid_data}")
        process_output = stream.process_batch(valid_data)
        stats = stream.get_stats()
        print(process_output)
        print(", ".join([f"{key}: {value}" for key, value in stats.items()]))


def main() -> None:
    event_input: List[Any] = [ "event: user_login",
                               "critical_error: database connection lost",
                                "alert: user_logout",
                                "error: high memory usage",
                                404,
                                None]
    transaction_input = [("buy", 800, "seed"),
                         ("sell", 322, "chickens"),
                         ("buy", 281, "fertilizer"),
                         ("buy", 91, "chicken_feed"),
                         ("sell", 183, "eggs")]
    sensor_input = [("temp", 28.7), ("temp", 12), ("temp", 9), ("temp", 19),
                    ("humidity", 65), ("humidity", 75), ("humidity", 55),
                    ("humidity", 70), ("pressure", 1013), ("pressure", 1200),
                    ("pressure", 1010), ("pressure", 950)]

    event_stream = EventStream("EVENT001")
    stream_processor = StreamProcessor()
    stream_processor.add_stream(event_stream)
    stream_processor.proccess_data("EVENT001", event_input, "error")
    transaction_stream = TransactionStream("TRANS_001", 9600)
    stream_processor.add_stream(transaction_stream)
    stream_processor.proccess_data("TRANS_001", transaction_input, "100")
    sensor_processor = SensorStream("SENSOR_001")
    stream_processor.add_stream(sensor_processor)
    stream_processor.proccess_data("SENSOR_001", sensor_input, "temp")


if __name__ == "__main__":
    main()
