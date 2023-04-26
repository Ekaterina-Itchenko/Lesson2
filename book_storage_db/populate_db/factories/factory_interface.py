from typing import Protocol


class FactoryProtocol(Protocol):
    def generate(self) -> object:
        raise NotImplementedError
