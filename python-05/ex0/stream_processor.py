from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return f"Output: Processed{result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        temp_lst = list()
        result = ""
        try:
            if self.validate(data):
                print("Validation: Numeric data verified")
                for x in data.split(','):
                    if x:
                        try:
                            temp_lst.append(int(float(x)))
                        except ValueError:
                            pass
            result = ", ".join([str(x) for x in temp_lst])
            return result
        except (ValueError, TypeError):
            return ""

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, result: str) -> str:
        try:
            total = sum(int(x) for x in result.split(','))
            average = total / len(result.split(','))
            return f"Output: Processed {len(result.split(','))} numeric values, \
sum={total} avg={average}"
        except (ValueError, TypeError):
            return "invalid data found"


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return ""

    def validate(self, data: Any) -> bool:
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return ""

    def validate(self, data: Any) -> bool:
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    numeric_processor = NumericProcessor()
    number = "9834.342, 12312, 123.1231,fdskj"
    numeric_res = numeric_processor.process(number)
    print(numeric_processor.format_output(numeric_res))


if __name__ == "__main__":
    main()
