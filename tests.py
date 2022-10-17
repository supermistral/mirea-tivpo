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


def test_size(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
              matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.size() == (2, 2)
    assert matrix_b_2x2.size() == (2, 2)
    assert matrix_a_3x3.size() == (3, 3)
    assert matrix_b_3x2.size() == (3, 2)


def test_minor(matrix_a_2x2: Matrix, matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.minor(1, 1) == 4
    assert matrix_a_2x2.minor(1, 2) == 3
    assert matrix_a_2x2.minor(2, 1) == 2
    assert matrix_a_2x2.minor(2, 2) == 1

    assert matrix_a_3x3.minor(1, 1) == -3
    assert matrix_a_3x3.minor(2, 2) == -12
    assert matrix_a_3x3.minor(3, 3) == -3

    with pytest.raises(ValueError):
        matrix_b_3x2.minor(1, 1)


def test_determinant(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                     matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.determinant() == -2
    assert matrix_b_2x2.determinant() == -8
    assert matrix_a_3x3.determinant() == 0
    
    with pytest.raises(ValueError):
        matrix_b_3x2.determinant()


def test_cofactor(matrix_a_2x2: Matrix, matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.cofactor(1, 1) == 4
    assert matrix_a_2x2.cofactor(1, 2) == -3
    assert matrix_a_2x2.cofactor(2, 1) == -2
    assert matrix_a_2x2.cofactor(2, 2) == 1

    assert matrix_a_3x3.cofactor(1, 1) == -3
    assert matrix_a_3x3.cofactor(1, 2) == 6
    assert matrix_a_3x3.cofactor(2, 2) == -12
    assert matrix_a_3x3.cofactor(2, 3) == 6
    assert matrix_a_3x3.cofactor(3, 3) == -3

    with pytest.raises(ValueError):
        matrix_b_3x2.cofactor(1, 1)
