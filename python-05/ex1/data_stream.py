from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


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
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        return ""

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    pass
