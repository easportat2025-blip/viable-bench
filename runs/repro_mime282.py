from mimesis.providers.numbers import Numbers


def test_primes_are_prime():
    got = list(Numbers.primes(2, 30))
    assert got == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], got
