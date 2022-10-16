import pytest

from main import Matrix


@pytest.fixture
def matrix_a_2x2():
    return Matrix([[1, 2], [3, 4]])


@pytest.fixture
def matrix_b_2x2():
    return Matrix([[2, 4], [6, 8]])


@pytest.fixture
def matrix_a_3x3():
    return Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


@pytest.fixture
def matrix_b_3x2():
    return Matrix([[0, 2], [4, 6], [8, 0]])


def test_determinant(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                     matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.determinant() == -2
    assert matrix_b_2x2.determinant() == -8
    assert matrix_a_3x3.determinant() == 0
    
    with pytest.raises(ValueError):
        matrix_b_3x2.determinant()
