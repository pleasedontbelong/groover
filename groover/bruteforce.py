from itertools import combinations

MAX_NB_TRACKS = 3


def tracks_match(tracks, concert_premiere_length):
    """
    Brute force, we'll generate all possible combinations of tracks taking
    groups of `MAX_NB_TRACKS` items
    """
    for combination in combinations(tracks, MAX_NB_TRACKS):
        if sum(t[1] for t in combination) == concert_premiere_length:
            return True
    return False
