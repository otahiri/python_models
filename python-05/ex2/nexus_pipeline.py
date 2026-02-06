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
        values = data.values()
        if len(values) > 3:
            values = list(values)[:-1]
        temp_output = " (critical range)" if "critical" in data.keys()\
            else " (normal range)"
        res = "Output: " + "".join([str(v) for v in values])
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
        print("Initializing Nexus Manager...")

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def add_stages(self, stages: List[ProcessingStage]):
        for pipeline in self.pipelines:
            for stage in stages:
                pipeline.add_stage(stage)

    def get_pipeline(self, id: str) -> Union[ProcessingPipeline, None]:
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == id:
                return pipeline
        return None

    def process_data(self, data: Any, id: str) -> None:
        pipeline = self.get_pipeline(id)
        if not pipeline:
            print("Warning: invalid pipeline_id")
            return
        output = pipeline.process(data)
        print(output) if output else print("")


class JSONAdapter(ProcessingPipeline):
    def process(self, data: str) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id} data through pipeline...")
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
        return output


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id} data through same pipeline...")
        try:
            res["sensor"] = data[0].split(":")[1]
            res["val"] = data[1].split(":")[1]
            res["unit"] = data[2].split(":")[1]
        except (ValueError, TypeError):
            print("Error: failure during the parsing stage")
            print("initializing safety protocol")
            print("closing all channels")
            return None
        output = super().run_stages(res)
        return output


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id} data through  pipeline...")
        try:
            elements = data.split(',')
            if len(elements) != 3:
                raise ValueError
            res["sensor"] = elements[0]
            res["val"] = elements[1]
            res["unit"] = elements[2]
        except (ValueError, KeyError, IndexError):
            print("Error: failure during the parsing stage")
            print("initializing safety protocol")
            print("closing all channels")
            return None
        output = super().run_stages(res)
        return output


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    nexus = NexusManager()
    json = JSONAdapter("JSON")
    csv = CSVAdapter("CSV")
    stream = StreamAdapter("Stream")
    nexus.add_pipeline(json)
    nexus.add_pipeline(csv)
    nexus.add_pipeline(stream)
    print("\nCreating Data Processing Pipeline..")
    input_stage = InputStage()
    tran_stage = TransformStage()
    output_stage = OutputStage()
    nexus.add_stages([input_stage, tran_stage, output_stage])
    print("\n=== Multi-Format Data Processing ===")
    nexus.process_data("{sensor: temp, val: 22.5, °C}", "JSON")
    nexus.process_data("temp, 35, °C", "CSV")
    nexus.process_data(["Initializing sensor: temp", "Received input: 111.9",
                        "Extracting reading unit: °C"], "Stream")
    print("Nexus Integration complete. All systems operational.")


main()
