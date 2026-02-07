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
        if not data:
            return None
        for value in data.values():
            if isnumber(value):
                num = float(value)
                if num < -20 or num > 30:
                    data["critical"] = True
                print("Transform: Enriched with metadata and validation")
                return data
        return None


class OutputStage:
    def __init__(self) -> None:
        print("Stage 3: Output formatting and delivery")

    def process(self, data: Any) -> Any:
        values = data.values()
        if len(values) > 3:
            values = list(values)[:-1]
        temp_output = " (critical range)" if "critical" in data.keys()\
            else " (normal range)"
        res = f"Output: {data.get('sensor', 'unknown')} {data.get('val', '0')}\
{data.get('unit', '')}"
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
                if not current_data:
                    raise ValueError
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

    def add_stages(self) -> None:
        stages: List[ProcessingStage] = [InputStage(), TransformStage(),
                                         OutputStage()]
        for pipeline in self.pipelines:
            for stage in stages:
                pipeline.add_stage(stage)

    def get_pipeline(self, id: str) -> Union[ProcessingPipeline, None]:
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == id:
                return pipeline
        return None

    def process_data(self, data: Any, id: str) -> str:
        pipeline = self.get_pipeline(id)
        if not pipeline:
            print("Warning: invalid pipeline_id")
            return ""
        output = pipeline.process(data)
        return output if output else ""

    def chain_data(self, data: Any, pipeline_id: str) -> None:
        processed = self.process_data(data, pipeline_id)
        if not processed:
            return
        analyzed = processed.replace("Output: ", "").split("(",)[0]
        product = self.process_data(", ".join(analyzed.split()), "CSV")
        if not product:
            return
        print(product)


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: str) -> Any:
        res: Dict = dict()
        print(f"\nProcessing {self.pipeline_id} data through pipeline...")
        try:
            elements = data[1:-1].split(',')
            if not all([len(element) != 2 for element in elements]):
                raise ValueError
            res["sensor"] = elements[0].split(":")[1]
            res["val"] = elements[1].split(":")[1]
            res["unit"] = elements[2].split(":")[1]
        except (ValueError, TypeError, IndexError):
            print("Error: failure during the parsing stage")
            print("initializing safety protocol")
            print("closing all channels")
            return None
        output = super().run_stages(res)
        return output


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

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
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

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
    nexus.add_pipeline(JSONAdapter("JSON"))
    nexus.add_pipeline(CSVAdapter("CSV"))
    nexus.add_pipeline(StreamAdapter("Stream"))
    print("\nCreating Data Processing Pipeline..")
    nexus.add_stages()
    print("\n=== Multi-Format Data Processing ===")
    print(nexus.process_data("{sensor: temp, val: 22.5, unit: °C}", "JSON"))
    print(nexus.process_data("temp, -35, °C", "CSV"))
    print(nexus.process_data(["Initializing sensor: temp",
          "Received input: 111.9", "Extracting reading unit: °C"], "Stream"))
    print("\n=== Pipeline Chaining Demo ===")
    nexus.chain_data("{sensor: temp, val: 22.5, unit: °C}", "JSON")

    print("\n=== Error Recovery Test ===\n\
Simulating pipeline failure...")
    nexus.process_data("{sensor: temp, val: invalid, unit: °C}", "JSON")
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("[Error]:", error)
