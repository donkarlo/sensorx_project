from typing import Annotated, Union
import numpy as np
import numpy.typing as npt
from mathx.linalg.matrix.vec import Vec

class TimeVal:
    def __init__(self, time:float, val:Union[np.ndarray, float, ] ):
        self._time = time
        self._val = val