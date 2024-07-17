"""Type utils functions"""

from typing import TypeVar, Generic, cast
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# Define a type variable for the dtype
DType = TypeVar("DType", bound=Axes)


# Little helper class, which is only used as a type.
class Array(np.ndarray, Generic[DType]):
    def __getitem__(self, key) -> DType:  # type: ignore
        return super().__getitem__(key)  # type: ignore


# Create the figure and axes
fig, _axs = plt.subplots(2, 2)

# Force assign the type, which is correct for most intents and purposes
axs: Array[Axes] = cast(Array[Axes], _axs)

# Now you should get method suggestions for Axes objects
axs[0, 0].plot()
