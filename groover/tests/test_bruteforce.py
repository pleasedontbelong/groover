from groover.bruteforce import tracks_match


def test_nominal():
    tracks = [("t1", 1), ("t2", 2), ("t3", 3), ("t4", 4), ("t5", 5)]
    assert tracks_match(tracks, 6)
    assert not tracks_match(tracks, 2)


def test_duplicated_time():
    """
    Test using multiple tracks with the same length
    """
    tracks = [("t1", 1), ("t2", 1), ("t3", 1), ("t4", 4), ("t5", 5)]
    assert tracks_match(tracks, 3)
