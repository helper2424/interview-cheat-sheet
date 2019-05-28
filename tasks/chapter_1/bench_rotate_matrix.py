from rotate_matrix import rotate_matrix, rotate_matrix_efficient
import timeit, functools
import numpy as np

if __name__ == "__main__":
    n = 1000
    big_image = np.random.rand(n,n)

    print("Benchmark for an unefficient version")
    t = timeit.Timer(functools.partial(rotate_matrix, big_image))
    print(t.timeit(5))

    print("Benchmark for an efficient version")
    t = timeit.Timer(functools.partial(rotate_matrix_efficient, big_image))
    print(t.timeit(5))