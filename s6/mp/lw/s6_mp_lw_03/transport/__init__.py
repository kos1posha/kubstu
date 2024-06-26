from .base import BaseTransportProblemSolver
from .mincost import MinimalCostTransportProblemSolver
from .nwc import NorthWestCornerTransportProblemSolver
from .vogels import VogelsApproximationTransportProblemSolver


MinCostSolver = MinimalCostTransportProblemSolver
NWCSolver = NorthWestCornerTransportProblemSolver
VogelsSolver = VogelsApproximationTransportProblemSolver
