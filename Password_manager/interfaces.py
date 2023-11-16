from typing import Protocol


class ExporterProto(Protocol):
    def export(self, value: dict[str, str]) -> None:
        raise NotImplementedError
