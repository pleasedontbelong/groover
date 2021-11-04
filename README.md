# Groover Test

## Algorithms

### Brute-force

I've created two brute force algorithms:

- the first one is `bruteforce.tracks_match` . It uses itertools.combinations to get all combinations of three tracks from the list and returns True if the sum of any of those combinations' sum is equal to `concert_premiere_length`.
- the second one is `bruteforce.tracks_match_recursive`. It's basically the same idea but without using itertools.combinations. It works but it generates more combinations than needed, so i stopped working on that since it's has the same complexity of the previous bruteforce algorithm. Also I should have used named tuples

### Optimized

`smart.tracks_match` works with a sorted list of tracks. It pops one item from the tracks list and then tries to find a pair of tracks so that the three numbers sum is equal to `concert_premiere_length`. It works something like this:

```
Loop 1
tracks = [1, 1, 4, 5]  concert_premiere_length = 6

- pop the last element from the tracks:
        current = 5       tracks = [1, 1, 4]
- try to find a pair of numbers on the remaining tracks where the sum is equal
  to (6 - current) = (6 - 5) = 1
        No pair found, repeat process with the remaining tracks

Loop 2
tracks = [2, 4, 4]  concert_premiere_length = 6

- pop the last element from the tracks:
        current = 4       tracks = [1, 1]
- try to find a pair of numbers on the remaining tracks where the sum is equal
  to (6 - current) = (6 - 4) = 2
        the pair (1, 1) is returned, return True because we found our list
```

### Optimized V2

`smart2.tracks_match` does not need to sort the list of tracks. Instead of generating combinations of tracks, it generates combinations of numbers that sum up to `concert_premiere_length`. We'll discard a combinations if we do not have a track length equal to the one of the combinations items. Something like:

```

tracks = [1, 1, 4, 5]  concert_premiere_length = 6

- we generate a map of the tracks where the key is the length and the value is
  the number of ocurrences of that length:
        length_distribution = {1: 2, 4: 1, 5: 1}


- Loop and generate all pair of numbers that sum up to 6 only if one of that pair
  is found on the `length_distribution`.
    possible_pairs:
        (1, 5) because 1 + 5 = 6 and because we find both 1 and 5 in `length_distribution`
        (2, 4) because 2 + 4 = 6 and because we find 4 in `length_distribution`
    - Loop 1 (1,5)
        we'll try to replace 5 with another tuple using the same condition as
        before. Posible tuples are (1, 4) and (2, 3). Since we do have both 1 and
        4 in the length_distribution we could return True. The final solution is
        (1, 1, 4)

```

I could have used recursivity for this algorith wich will allow us to go deeper and get more than 3 tracks.

# Development

## Install on development mode

In order to launch the tests, you must install the packages inside `requirements.dev.txt`.

Inside a virtualenv call:

```sh
pip install -r requirements.dev.txt
```

## Tests

Tests were made with pytest using coverage.

```sh
pytest .
```

You can also launch the tests on different python versions:

```sh
tox
```

## Lint

Currently using `flake8` for checking pep8 and autoformatting using `black`.

```sh
flake8 .
black . --check
```

Started 22h05
