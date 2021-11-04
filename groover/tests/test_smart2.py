import pytest
from groover.smart2 import (
    tracks_match,
    _get_two_number_combinations,
    _generate_distribution,
)


@pytest.mark.parametrize(
    "tracks,total_length",
    [
        ([3, 4, 5, 6, 6, 9], 15),
        ([1, 1, 2, 6, 6, 9], 4),
        ([1, 1, 1, 6, 6, 9], 3),
        ([1, 1, 1, 1, 6, 9], 3),
        ([3, 3, 3, 7, 8, 9], 9),
    ],
)
def test_found_three(tracks, total_length):
    assert tracks_match(tracks, total_length)


@pytest.mark.parametrize(
    "tracks,total_length",
    [([3, 4, 5, 6, 6, 9], 100), ([1, 1, 2, 6, 6, 9], 1), ([1, 1, 1, 6, 6, 9], 0)],
)
def test_not_found_three(tracks, total_length):
    assert not tracks_match(tracks, total_length)


@pytest.mark.parametrize(
    "number,expected",
    [
        [0, [(0, 0)]],
        [3, [(1, 2)]],
        [6, [(3, 3), (1, 5), (2, 4)]],
        [10, [(5, 5), (1, 9), (2, 8), (3, 7), (4, 6)]],
    ],
)
def test_get_two_number_combinations(number, expected):
    length_distribution = {i: 2 for i in range(10)}
    assert list(_get_two_number_combinations(length_distribution, number)) == expected


@pytest.mark.parametrize(
    "tracks,expected",
    [
        [[1, 2, 3], {1: 1, 2: 1, 3: 1}],
        [[1, 1, 1], {1: 3}],
        [[5], {5: 1}],
    ],
)
def test_generate_distribution(tracks, expected):
    assert _generate_distribution(tracks) == expected
