from itertools import chain
from random import choice, sample

from pynvim import Nvim
from pynvim_pp.lib import write

from ...registry import rpc

_CHARS = range(3, 6)
_ANNOUNCE = (
    "🥚",
    "🐥",
    "🐣",
    "🐤",
    "🐓",
    "🐔",
)
_STARS = (
    "✨",
    "💫",
    "⭐️",
    "🌟",
    "☄️",
)


@rpc(blocking=True)
def now(nvim: Nvim, *_: None) -> None:
    chars = choice(_CHARS)
    star = choice(_STARS)
    msg = " ".join(chain((star,), sample(_ANNOUNCE, k=chars), (star,)))
    write(nvim, msg)
