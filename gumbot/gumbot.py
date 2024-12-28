from __future__ import annotations

from collections.abc import Callable
from typing import Literal, TypeVar, Any, List

from functools import wraps

import time

from ahk import AHK

ReturnType = TypeVar('ReturnType')

def requires_roblox_activated(f: Callable[[Gumbot, ...], ReturnType]):
    @wraps(f)
    def wrapped(self: Gumbot, *args, **kwargs) -> ReturnType:
        self.activate_roblox()
        time.sleep(self.input_delay)
        f(self=self, *args, **kwargs)
    
    return wrapped

class Gumbot:
    def __init__(self, ahk: AHK[Literal['v2']], input_delay: float = 0.1) -> None:
        """
        ahk: The instance of Autohotkey.
        input_delay: The delay between inputs in seconds.
        """
        self.ahk = ahk
        self.input_delay = input_delay
    
    def join_place(self, place_id: int) -> None:
        from webbrowser import open

        open(f"roblox://placeID={place_id}")
    
    def join_place_with_link_code(self, place_id: int, link_code: int) -> None:
        from webbrowser import open

        open(f"roblox://placeID={place_id}&linkCode={link_code}")

    def join_user(self, user_id: int) -> None:
        raise NotImplementedError()
    
    @requires_roblox_activated
    def leave_place(self) -> None:
        self.ahk.send('{Esc}')
        time.sleep(self.input_delay)
        self.ahk.send('L')
        time.sleep(self.input_delay)
        self.ahk.send('{Enter}')

    @requires_roblox_activated
    def respawn_character(self) -> None:
        self.ahk.send('{Esc}')
        time.sleep(self.input_delay)
        self.ahk.send('R')
        time.sleep(self.input_delay)
        self.ahk.send('{Enter}')
    
    def activate_roblox(self) -> None:
        self.ahk.win_activate("Roblox")

