from typing import TypedDict, Callable, Optional


class UrlMap(TypedDict):
    url: str
    view: Callable
    name: str
    distill_file: Optional[str]
    distill_func: Optional[Callable]
