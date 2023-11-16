from typing import Protocol, Any


class ProviderProto(Protocol):
    def __call__(self, *args) -> Any:
        raise NotImplementedError
