from typing import Self

class UiState:
    def __init__(self):
        raise NotImplementedError()

    def render(self):
        raise NotImplementedError()

    def input(self) -> Self | None:
        raise NotImplementedError()
