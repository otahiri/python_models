# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    nexus_pipeline.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otahiri- <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/04 13:50:25 by otahiri-          #+#    #+#              #
#    Updated: 2026/02/04 13:50:27 by otahiri-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod


def isnumber(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def __init__(self) -> None:
        print("Stage 1: Input validation and parsing")

    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print(f"Input: {data}")
            return data
        return None


class TransformStage:
    def __init__(self) -> None:
        print("Stage 2: Data transformation and enrichment")

    def process(self, data: Any) -> Any:
        for value in data.values():
            if isnumber(value):
                num = float(value)
                if num > 30:
                    data["critical"] = True
                    break
        print("Transform: Enriched with metadata and validation")
        return data


class OutputStage:
    def __init__(self) -> None:
        print("Stage 3: Output formatting and delivery")

    def process(self, data: Any) -> Any:
        keys = list(data.keys())
        if len(keys) > 2:
            keys = keys[:-1]
        temp_output = " (critical range)" if "critical" in keys\
            else " (normal range)"
        res = "Output: " + "".join([str(v) for v in list(data.values())])
        return res + temp_output


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
        current_data: Optional[dict] = data
        idx = 0
        for stage in self.stages:
            idx += 1
            try:
                current_data = stage.process(current_data)
            except (ValueError, KeyError):
                print(f"Error detected in Stage {idx}: Invalid data format")
                print("Recovery initiated: Switching to backup processor")
                current_data = None
                print("Recovery successful: Pipeline \
restored, processing resumed")
                return current_data
        return current_data


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def get_pipeline(self, id: str) -> Union[ProcessingPipeline, None]:
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == id:
                return pipeline
        return None

    def process_all(self, data: Any, id: str) -> None:
        pipeline = self.get_pipeline(id)
        if not pipeline:
            print("Warning: invalid pipeline_id")
            return
        pipeline.process(data)


class JSONAdapter(ProcessingPipeline):
    def process(self, data: str) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id}, data through pipeline...")
        try:
            elements = data[1:-1].split(',')
            for element in elements:
                key, value = element.split(":")
                res[key] = value
        except (ValueError, TypeError):
            print("Error: failure during the parsing stage")
            print("initializing safety protocol")
            print("closing all channels")
            return None
        output = super().run_stages(res)
        if not output:
            return None
        return output


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id}, data through  pipeline...")
        try:
            elements = data.split(',')
            res["sensor"] = elements[0]
            res["value"] = elements[1]
            res["unit"] = elements[2]
        except (ValueError, KeyError, IndexError):
            print("Error: failure during the parsing stage")
            print("initializing safety protocol")
            print("closing all channels")
            return None
        output = super().run_stages(res)
        return output


def main() -> None:
    json = JSONAdapter("JSON001")
    input_stage = InputStage()
    tran_stage = TransformStage()
    output_stage = OutputStage()
    json.add_stage(input_stage)
    json.add_stage(tran_stage)
    json.add_stage(output_stage)
    print("\n=== Multi-Format Data Processing ===\n")
    json_output = json.process("{sensor: temp, val: 22.5, unit: °C}")
    print(json_output) if json_output else print("")
    csv = CSVAdapter("CSV")
    csv.add_stage(input_stage)
    csv.add_stage(tran_stage)
    csv.add_stage(output_stage)
    csv_output = csv.process("temp, 35, °C")
    print(csv_output)


main()
