
def sum_up_to(n: int) -> int:
    count = 0
    for i in range(n):
        count += i + 1

    return count


if __name__ == '__main__':

    # Parse these command line arguments
    # - n: integer, number to count up to
    # - threads: integer, number of threads to use
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('number', type=int, default=100)
    # add a flag to enable numpy usage or not
    parser.add_argument('--numpy', action='store_true', default=False)
    args = parser.parse_args()

    # time the count function
    from time import time
    start = time()
    if args.numpy:
        print('using numpy')
        import numpy as np
        result = np.sum(np.arange(args.number + 1))
    else:
        result = sum_up_to(args.number)

    
    # print(f'sum up to {args.number} is {result} took {time() - start} seconds')
    print(f'sum up to {args.number} is {result}')