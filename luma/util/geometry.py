from typing import Iterable
import numpy as np
from math import sin, cos

def getRotationMatrix(rot: Iterable[float]) -> np.array:
    """ Generate the 3D rotation matrix for the
        given xzx rotation triplet.
    """ 
    gamma = rot[0]
    beta = rot[1]
    alpha = rot[2]

    sg = sin(gamma)
    cg = cos(gamma)
    sb = sin(beta)
    cb = cos(beta)
    sa = sin(alpha)
    ca = cos(alpha)

    row1 = [cb, -cg*sb, sb*sg]
    row2 = [ca*sb, (ca*cb*cg) - (sa * sg), (-cg*sa) - (ca*cb*sg)]
    row3 = [sa*sb, (ca*sg) + (cb*cg*sa), (ca*cg) - (cb*sa*sg)]

    return np.array([row1, row2, row3])

def asHomogeneous(vec: np.array) -> np.array:
    """ Given 3D coordinates, generate the 4D homogeneous
        coordinates.
    """

    return np.append(vec, 1.0)
