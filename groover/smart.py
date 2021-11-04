def tracks_match(tracks, concert_premiere_length):
    """
    Proxy for _find_three_tracks, just to be sure we sort the list
    before calling it
    """
    # first we need to sort the track lengths
    tracks.sort()
    return _find_three_tracks(tracks, total_length=concert_premiere_length)


def _find_three_tracks(tracks, total_length):
    """
    Returns True if the sum of three tracks on the `tracks` list are
    equal to `concert_premiere_length`
    """
    if len(tracks) < 3:
        return False

    last = tracks.pop()
    # find two tracks with the length equal to (total_length - last)
    if _find_two_tracks(tracks, total_length - last):
        return True
    else:
        # the last track is useless, we repeat the operation without it
        return _find_three_tracks(tracks, total_length)


def _find_two_tracks(tracks, total_length):
    """
    Finds two tracks that have a sum equal to total_length.
    We assume the tracks are sorted.
    """
    if len(tracks) < 2:
        return False

    # the max sum we can get is the sum of the first and the last element
    max_sum = tracks[0] + tracks[-1]
    # if that sum is equal to `total_length` we have our solution
    if max_sum == total_length:
        return True
    # if the sum is lower, then we repeat the opearion without the first element
    elif max_sum < total_length:
        return _find_two_tracks(tracks[1:], total_length)
    # if the sum is higher, then we repeat the opearion without the last element
    elif max_sum > total_length:
        return _find_two_tracks(tracks[:-1], total_length)
