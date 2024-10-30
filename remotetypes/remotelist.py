"""Needed classes to implement and serve the RList type."""

from typing import Optional

import Ice
import RemoteTypes as rt  # noqa: F401; pylint: disable=import-error

from remotetypes.customset import StringSet
from remotetypes.iterable import Iterable



class RemoteList(rt.RList):
    """Skelenton for the RList implementation."""
    def __init__(self) -> None:
        """Initialise a RemoteSet with an empty StringSet."""
        self._storage_ = StringSet()

    def remove(self, item: str, current: Optional[Ice.Current] = None) -> None:
        """Remove an item from the StringSet if added. Else, raise a remote exception."""
        try:
            self._storage_.remove(item)
        except KeyError as error:
            raise rt.KeyError(item) from error

    def length(self, current: Optional[Ice.Current] = None) -> int:
        """Return the number of elements in the StringSet."""
        return len(self._storage_)

    def contains(self, item: str, current: Optional[Ice.Current] = None) -> bool:
        """Check the pertenence of an item to the StringSet."""
        return item in self._storage_

    def hash(self, current: Optional[Ice.Current] = None) -> int:
        """Calculate a hash from the content of the internal StringSet."""
        contents = list(self._storage_)
        contents.sort()
        return hash(repr(contents))
    
    def iter(self, current: Optional[Ice.Current] = None) -> rt.IterablePrx:
        """Create an iterable object."""
        iterator = Iterable(self._storage_)
        adapter = current.adapter
        proxy = adapter.addWithUUID(iterator)
        return rt.IterablePrx.checkedCast(proxy)
    
    def append(self, item: str, current: Optional[Ice.Current] = None) -> None:
        self._storage_.append(item)

    def pop(self, index: Optional[int] = None, current: Optional[Ice.Current] = None) -> str:
        try:
            if index is None:
                return self._storage_.pop()
            
            return self._storage_.pop(index)
        
        except IndexError as exec:
            raise rt.IndexError("Valor fuera del rango") from exec
        
    def getItem(self, index: int, current: Optional[Ice.Current] = None) -> str:
        try:
            return self._storage_[index]
        
        except IndexError as exec:
            raise rt.IndexError("Valor fuera del rango") from exec