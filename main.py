from typing import List, Tuple


class Matrix:
    def __init__(self, matrix: List[List[float]]):
        self.matrix = matrix

    def _determinant_helper(self) -> float:
        pass

    def _minor(self) -> float:
        pass

    def _cofactor(self) -> float:
        pass

    def size() -> Tuple[int, int]:
        pass

    def determinant(self) -> float:
        pass

    def minor(self, r: str, c: str) -> float:
        pass

    def cofactor(self, r: str, c: str) -> float:
        pass
