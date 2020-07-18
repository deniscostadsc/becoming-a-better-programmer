from typing import Optional


class Node:
    def __init__(self) -> None:
        self.value: Optional[int] = None
        self.next = None
