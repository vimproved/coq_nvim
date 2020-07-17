from dataclasses import dataclass
from typing import Any, AsyncIterator, Callable, Dict, Optional

from pynvim import Nvim


@dataclass
class SourceSpec:
    main: str
    short_name: str
    enabled: bool
    priority: Optional[float]
    limit: Optional[float]
    timeout: Optional[float]
    config: Optional[Any]


@dataclass(frozen=True)
class Settings:
    sources: Dict[str, SourceSpec]


@dataclass(frozen=True)
class SourceSeed:
    limit: float
    timeout: float
    config: Optional[Any] = None


@dataclass(frozen=True)
class Position:
    row: int
    col: int


@dataclass(frozen=True)
class SourceFeed:
    position: Position


@dataclass(frozen=True)
class SourceCompletion:
    text: str
    priority: Optional[int] = None
    display: Optional[str] = None
    detail: Optional[str] = None


Source = Callable[[SourceFeed], AsyncIterator[SourceCompletion]]
Factory = Callable[[Nvim, SourceSeed], AsyncIterator[Source]]


@dataclass(frozen=True)
class SourceFactory:
    name: str
    short_name: str
    priority: float
    timeout: float
    limit: float
    seed: SourceSeed
    manufacture: Factory
