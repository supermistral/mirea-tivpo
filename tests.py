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


def test_is_square(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                   matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.is_square()
    assert matrix_b_2x2.is_square()
    assert matrix_a_3x3.is_square()
    assert not matrix_b_3x2.is_square()


def test_get_matrix(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                    matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    assert matrix_a_2x2.get_matrix() == [[1, 2], [3, 4]]
    assert matrix_b_2x2.get_matrix() == [[2, 4], [6, 8]]
    assert matrix_a_3x3.get_matrix() == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert matrix_b_3x2.get_matrix() == [[0, 2], [4, 6], [8, 0]]


def test_multiplication_by_number(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                                  matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    new_matrix_a_2x2 = matrix_a_2x2 * 2
    new_matrix_b_2x2 = matrix_b_2x2 * 2
    new_matrix_a_3x3 = matrix_a_3x3 * 5
    new_matrix_b_3x2 = matrix_b_3x2 * 10

    assert isinstance(new_matrix_a_2x2, Matrix)
    assert isinstance(new_matrix_b_2x2, Matrix)
    assert isinstance(new_matrix_a_3x3, Matrix)
    assert isinstance(new_matrix_b_3x2, Matrix)

    assert new_matrix_a_2x2.size() == (2, 2)
    assert new_matrix_b_2x2.size() == (2, 2)
    assert new_matrix_a_3x3.size() == (3, 3)
    assert new_matrix_b_3x2.size() == (3, 2) 
    assert new_matrix_a_2x2.get_matrix() == [[2, 4], [6, 8]]
    assert new_matrix_b_2x2.get_matrix() == [[4, 8], [12, 16]]
    assert new_matrix_a_3x3.get_matrix() == [[5, 10, 15], [20, 25, 30], [35, 40, 45]]
    assert new_matrix_b_3x2.get_matrix() == [[0, 20], [40, 60], [80, 0]]


def test_multiplication_by_matrix(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                                  matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    new_matrix_a_2x2 = matrix_a_2x2 * matrix_b_2x2
    new_matrix_a_3x2 = matrix_a_3x3 * matrix_b_3x2

    assert isinstance(new_matrix_a_2x2, Matrix)
    assert isinstance(new_matrix_a_3x2, Matrix)

    assert new_matrix_a_2x2.size() == (2, 2)
    assert new_matrix_a_3x2.size() == (3, 2) 
    assert new_matrix_a_2x2.get_matrix() == [[14, 20], [30, 44]]
    assert new_matrix_a_3x2.get_matrix() == [[32, 14], [68, 38], [104, 62]]

    with pytest.raises(ArithmeticError):
        matrix_a_2x2 * matrix_a_3x3


def test_addition(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                  matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    new_matrix_a_2x2 = matrix_a_2x2 + matrix_b_2x2
    new_matrix_a_3x3 = matrix_a_3x3 + matrix_a_3x3

    assert isinstance(new_matrix_a_2x2, Matrix)
    assert isinstance(new_matrix_a_3x3, Matrix)

    assert new_matrix_a_2x2.size() == (2, 2)
    assert new_matrix_a_3x3.size() == (3, 3) 
    assert new_matrix_a_2x2.get_matrix() == [[3, 6], [9, 12]]
    assert new_matrix_a_3x3.get_matrix() == [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

    with pytest.raises(ArithmeticError):
        matrix_a_2x2 + matrix_b_3x2

def test_subtraction(matrix_a_2x2: Matrix, matrix_b_2x2: Matrix,
                     matrix_a_3x3: Matrix, matrix_b_3x2: Matrix):
    new_matrix_a_2x2 = matrix_a_2x2 - matrix_b_2x2
    new_matrix_a_3x3 = matrix_a_3x3 - matrix_a_3x3

    assert isinstance(new_matrix_a_2x2, Matrix)
    assert isinstance(new_matrix_a_3x3, Matrix)

    assert new_matrix_a_2x2.size() == (2, 2)
    assert new_matrix_a_3x3.size() == (3, 3) 
    assert new_matrix_a_2x2.get_matrix() == [[-1, -2], [-3, -4]]
    assert new_matrix_a_3x3.get_matrix() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    with pytest.raises(ArithmeticError):
        matrix_a_2x2 - matrix_b_3x2
