def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n-1)


if __name__ == '__main__':
    print(recursive_sum(100))
