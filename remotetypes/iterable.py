"""Needed classes for implementing the Iterable interface for different types of objects."""
from typing import List, Optional

import Ice
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error

# TODO: It's very likely that the same Iterable implementation doesn't fit
# for the 3 needed types. It is valid to implement 3 different classes implementing
# the same interface and use an object from different implementations when needed.


class Iterable(rt.Iterable):
    """Skeleton for an Iterable implementation."""
    def __init__(self, elements: List[str]):
        self.elements = elements
        self.index = 0
        self.hash_inicial = hash(repr(elements))

    def next(self, current: Optional[Ice.Current] = None) -> str:
        if hash(repr(self.elements)) != self.hash_inicial:
            raise rt.CancelIteration()
        
        if self.index >= len(self.elements):
            raise rt.StopIteration()
        
        element = self.elements[self.index]
        self.index += 1
        return element
