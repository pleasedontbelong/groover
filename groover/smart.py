from groover.bruteforce import MAX_NB_TRACKS


def tracks_match(tracks, concert_premiere_length):
    """
    Returns True if the sum of three tracks on the `tracks` list are
    equal to `concert_premiere_length`
    """
    # generate an array of False with length equal to concert_premiere_length
    results = [False for i in range(concert_premiere_length + 1)]
    # for each index we'll find if there's a sum of two tracks that are equal
    # to the index
    for i in range(len(results)):
        results[i] = _find_two_tracks(tracks, i)

    # loop over every track and we'll use the results array to check if there's
    # a pair of tracks that have a sum equal to the difference of the `concert_premiere_length`
    # and the `track`
    for track in tracks:
        try:
            if results[concert_premiere_length - track]:
                return True
        except IndexError:
            continue
    return False


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
