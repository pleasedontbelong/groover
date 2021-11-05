def tracks_match(tracks, concert_premiere_length):
    """
    It generates all possible sums of numbers checking if a number of the
    combination is present in the tracks list
    """
    length_distribution = _generate_distribution(tracks)
    return _find_three_tracks(length_distribution, concert_premiere_length)


def _find_three_tracks(length_distribution, max_length, chosen=None):
    if chosen is None:
        chosen = []

    for number1, number2 in _get_two_number_combinations(
        length_distribution, max_length
    ):
        if chosen and number1 in length_distribution and number2 in length_distribution:
            return True

        if number2 not in length_distribution:
            to_replace = number2
            to_keep = number1
        else:
            to_replace = number1
            to_keep = number2
        # try to replace one of the numbers with another combination of
        # two numbers.
        # first we need to copy and remove the number1 from the distribution
        new_distribution = length_distribution.copy()
        new_distribution[to_keep] -= 1
        chosen.append(to_keep)
        if _find_three_tracks(new_distribution, to_replace, chosen):
            return True


def _generate_distribution(tracks):
    """
    Returns a dict where the key is a length track and the value is the number
    of times the length of the track is present on the `tracks` list
    """
    length_distribution = {}

    for track_duration in tracks:
        length_distribution[track_duration] = (
            length_distribution.get(track_duration, 0) + 1
        )

    return length_distribution


def _get_two_number_combinations(length_distribution, number):
    """
    Genereates a list of tuples of numbers that sum up to the `number`
    but only if one of those numbers are included in the length_distribution
    """
    if number % 2 == 0 and length_distribution.get(number / 2, 0) >= 2:
        yield (int(number / 2), int(number / 2))
    for i in range(1, int((number - 1) / 2) + 1):
        complement = number - i
        if length_distribution.get(i) or length_distribution.get(complement):
            yield (i, complement)
