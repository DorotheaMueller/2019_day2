from maxima import find_maxima
import pytest
import numpy as np

test_cases = [
	([-i**2 for i in range(-3, 4)], [3]),
	([np.sin(2*alpha) for alpha in np.linspace(0.0, 5.0, 100)], [16, 78]),
	([0, 1, 2, 1, 2, 1, 0], [2, 4]),
	([4, 2, 1, 3, 1, 2], [0, 3, 5]),
   ([4, 2, 1, 3, 1], [0, 3]),
   ([1, 2, 2, 1], [1, 2]),
   ([1, 2, 2, 3, 1], [1, 3]),
   ([1, 3, 2, 2, 1], [1, 3]),
   ([3, 2, 2, 3], [0, 3]),
   ([3, 2, 2, 2, 3], [0, 2, 4])
]

test_cases_indice_edges = [
	([], []),
	([1, 0], [0]),
	([0, 1], [1]),
	([4, 2, 3], [0, 2]),
	([4, 2, 1, 3, 1, 2], [0, 3, 5]),
]


@pytest.mark.xfail
def test_string_input():
	out = find_maxima(['asdf'])

@pytest.mark.parametrize('inp, exp', test_cases_indice_edges)
def test_indices_edge(inp, exp):
	out = find_maxima(inp)
	assert out == exp

@pytest.mark.parametrize('inp, exp', test_cases)
def test_maxima_simple_input(inp, exp):
	out = find_maxima(inp)
	assert out == exp
	