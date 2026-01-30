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


class StreamProcessor:
    pass
