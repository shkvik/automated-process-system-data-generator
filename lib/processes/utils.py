import random
import decimal



def drange(x, y, jump):
  while x < y:
    yield float(x)
    x += decimal.Decimal(jump)


def compress(list: list[float]):
    bias = min(list)
    list = [y + abs(bias) for y in list]
    denominator = max(list) / 100
    list = [y / denominator for y in list]
    return list

def constrained_sum_sample_pos(n, total):
    """Return a randomly chosen list of n positive integers summing to total.
    Each such list is equally likely to occur."""

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [a - b for a, b in zip(dividers + [total], [0] + dividers)]
