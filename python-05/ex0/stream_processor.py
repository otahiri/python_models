from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        temp_lst: List = list()
        result = ""
        try:
            if self.validate(data):
                print("Validation: Numeric data verified")
                if data.__class__.__name__ == "list":
                    for x in data:
                        if x and x.__class__.__name__ in ["int", "float"]:
                            try:
                                temp_lst.append(int(x))
                            except ValueError:
                                pass
                elif data.__class__.__name__ in ["int", "float"]:
                    temp_lst.append(int(data))
            else:
                print("Warning: data is invalid")
            result = ", ".join([str(x) for x in temp_lst])
            return result
        except (ValueError, TypeError):
            return ""

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "list" and\
                (all(x.__class__.__name__ in ["int", "float"] for x in data)
                    or data.__class__.__name__ in ["float", "int"])

    def format_output(self, result: str) -> str:
        try:
            total = sum(int(x) for x in result.split(','))
            average = total / len(result.split(','))
            return f"Output: Processed {len(result.split(','))} numeric \
values, sum={total} avg={average}"
        except (ValueError, TypeError):
            return "invalid data found"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        total = ""
        if self.validate(data):
            print("Validation: Text data verified")
            total = " ".join([w for w in data.split() if not w.isdigit()])
            return total

        return "invalid"

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "str"

    def format_output(self, result: str) -> str:
        if result == "invalid":
            return "invalid text detected"
        char_count: Optional[int] = 0
        word_count: Union[int, None] = 0
        word_count += len(result.split(' '))
        char_count += len([x for w in result.split(' ') for x in w])
        return f"Output: Processed text: {char_count} \
characters, {word_count} words"


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        res: Dict = {"Warning": [], "Error": [], "Log": []}
        if self.validate(data):
            print(f"Processing data: \"{data}\"")
            print("Validation: Log entry verified")
            try:
                for log in data:
                    if "Warning" in log:
                        res["Warning"].append(log)
                if res["Warning"]:
                    return "Alert: critical state detected"
                else:
                    return "everything is working perfectly"
            except (KeyError, ValueError):
                return "invalid data"
        return "invalid data"

    def validate(self, data: Any) -> bool:
        valid = data.__class__.__name__ == "list" and \
            all(x.__class__.__name__ == "str" for x in data)
        return valid

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("\nInitializing Numeric Processor...")
    numeric_processor = NumericProcessor()
    number = [9834.342, 12312, 123.1231]
    numeric_res = numeric_processor.process(number)
    print(numeric_processor.format_output(numeric_res))
    print("\nInitializing Text Processor...")
    text_processor = TextProcessor()
    text = "hello world 832 my name is me"
    text_res = text_processor.process(text)
    print(text_processor.format_output(text_res))
    print("\nInitializing Log Processor...")
    log_processor = LogProcessor()
    logs: List = ["Alert server is under load",
                  "Alert: server is down",
                  "Warning: connection time out"]
    log_res = log_processor.process(logs)
    print(log_processor.format_output(log_res))
    processors = [numeric_processor, text_processor, log_processor]
    print("\n=== Polymorphic Processing Demo ===")
    print()
    result = processors[0].process(number)
    print("Result 0: ", processors[0].format_output(result))
    print()
    result = processors[1].process(text)
    print("Result 1: ", processors[1].format_output(result))
    print()
    result = processors[2].process(logs)
    print("Result 2: ", processors[2].format_output(result))


if __name__ == "__main__":
    main()
