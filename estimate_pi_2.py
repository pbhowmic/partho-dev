import numpy as np


def inside_circle(x: float, y: float) -> bool:
    return x**2 + y**2 - 1 < 0


def estimate_pi_1stqaud(n=1000000):
    nums = np.random.random_sample((n, 2))

    insides = np.array([1 if inside_circle(x, y) else 0 for x, y in nums])
    mean = np.mean(insides)
    sd = np.std(insides)
    return 4 * mean, 4 * sd


if __name__ == "__main__":
    estimate_pi_1stqaud()
