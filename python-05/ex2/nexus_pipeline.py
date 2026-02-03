from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print(f"Input: {data}")
            return data
        return None


class TransformStage:
    def process(self, data: Any) -> Any:
        for value in data.values():
            if isinstance(value, int):
                if value > 30:
                    data["critical"] = True
        print("Transform: Enriched with metadata and validation")
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        res = f"Output: {}"

class ProcessingPipeline (ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...

    def run_stages(self, data: Any) -> Any:
        current_data = data
        for stage in self.stages:
            current_data = stage.process(data)
        return current_data


class JSONAdapter(ProcessingPipeline):
    def process(self, data: str) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id} data through pipeline...")
        element = data.split(',')
        if len(element) != 2:
            raise ValueError
        sensor = element[0].split(':')
        val = element[1].split(':')
        if len(sensor) != 2 or len(val) != 2:
            raise ValueError
        key, value = sensor
        res[key] = value
        key, value = val
        res[key] = value
        self.run_stages(res)
