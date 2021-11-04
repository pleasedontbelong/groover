import pytest
from groover.smart import _find_three_tracks, _find_two_tracks


@pytest.mark.parametrize(
    "tracks,total_length",
    [
        ([3, 4, 5, 6, 6, 9], 10),
        ([1, 1, 2, 6, 6, 9], 8),
        ([1, 1, 1, 6, 6, 9], 2),
        ([0, 1, 1, 1, 6, 9], 1),
        ([0, 1, 2, 3, 3, 4, 5], 6),
    ],
)
def test_found_two(tracks, total_length):
    assert _find_two_tracks(tracks, total_length)


@pytest.mark.parametrize(
    "tracks,total_length",
    [
        ([3, 4, 5, 6, 6, 9], 100),
        ([1, 1, 2, 6, 6, 9], 1),
        ([1, 1, 1, 6, 6, 9], 0),
        ([0, 1, 1, 1, 6, 9], 8),
    ],
)
def test_not_found_two(tracks, total_length):
    assert not _find_two_tracks(tracks, total_length)


@pytest.mark.parametrize(
    "tracks,total_length",
    [
        ([3, 4, 5, 6, 6, 9], 15),
        ([1, 1, 2, 6, 6, 9], 4),
        ([1, 1, 1, 6, 6, 9], 3),
        ([1, 1, 1, 1, 6, 9], 3),
        ([0, 1, 1, 3, 6, 9], 2),
    ],
)
def test_found_three(tracks, total_length):
    assert _find_three_tracks(tracks, total_length)


@pytest.mark.parametrize(
    "tracks,total_length",
    [
        ([3, 4, 5, 6, 6, 9], 100),
        ([1, 1, 2, 6, 6, 9], 1),
        ([1, 1, 1, 6, 6, 9], 0),
        ([3, 3, 3, 3, 3, 3], 3),
    ],
)
def test_not_found_three(tracks, total_length):
    assert not _find_three_tracks(tracks, total_length)
