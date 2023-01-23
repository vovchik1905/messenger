from __future__ import annotations
import inspect
from enum import IntEnum

class State(IntEnum):
    ANY = 0

#A = IntEnum(value="A", names = [('a', 1), ('b', 2), ('c', 3)])
#print(A.a)

#class ServerState(IntEnum):
#    pass

class ServerState:
    _object_counter: int = 0
    
    def __init__(self) -> None:
        self._object_counter += 1
        self.value = self._object_counter

    def __add__(self, other: ServerState) -> ServerState:
        if (self.value + other.value) <= self._object_counter:
            pass


class ServerStateGroup:
    @classmethod
    def set(cls) -> None:
        pass
    
    @classmethod
    def current(cls) -> ServerState:
        pass

    @classmethod
    def next(cls) -> ServerState | None:
        pass

    @classmethod
    def previous(cls) -> ServerState | None:
        pass

    @classmethod
    def first(cls) -> ServerState | None:
        pass

    @classmethod
    def last(cls) -> ServerState | None:
        pass


class MessenderStates:
    A = ServerState()
    B = ServerState()
    C = ServerState()