from itertools import combinations

MAX_NB_TRACKS = 3
AUX = 0


def tracks_match(tracks, concert_premiere_length):
    """
    Brute force, we'll generate all possible combinations of tracks taking
    groups of `MAX_NB_TRACKS` items
    """
    for combination in combinations(tracks, MAX_NB_TRACKS):
        if sum(t[1] for t in combination) == concert_premiere_length:
            return True
    return False


def tracks_match_recursive(tracks, concert_premiere_length, chosen_tracks=None):
    """
    Recursive way without using itertools.combination, the complexity is the same
    but the code is awfuly worst
    """
    if chosen_tracks is None:
        chosen_tracks = []
    if len(tracks) + len(chosen_tracks) < MAX_NB_TRACKS:
        return False
    elif (
        len(chosen_tracks) == MAX_NB_TRACKS
        and sum(t[1] for t in chosen_tracks) == concert_premiere_length
    ):
        return True
    elif len(chosen_tracks) < MAX_NB_TRACKS:
        chosen_tracks.append(tracks.pop())
        return tracks_match_recursive(tracks, concert_premiere_length, chosen_tracks)
    elif len(chosen_tracks) == MAX_NB_TRACKS:
        if tracks_match_recursive(
            tracks + [chosen_tracks[1]], concert_premiere_length, [chosen_tracks[0]]
        ):
            return True
        elif tracks_match_recursive(
            tracks + [chosen_tracks[2]], concert_premiere_length, [chosen_tracks[0]]
        ):
            return True
        else:
            del chosen_tracks[0]
            return tracks_match_recursive(
                tracks + chosen_tracks, concert_premiere_length
            )
