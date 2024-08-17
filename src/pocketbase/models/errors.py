from typing import Any


class PocketBaseError(Exception):
    def __init__(self, url: str, status: int, data: Any) -> None:
        self.url = url
        self.status = status
        self.data = data

    def __repr__(self) -> str:
        return f"PocketBaseError(url={self.url},status={self.status},data={self.data})"

    __str__ = __repr__
