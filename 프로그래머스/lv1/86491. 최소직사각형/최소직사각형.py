def solution(sizes):
    long = []
    short = []
    for pair in sizes:
        long.append(max(pair))
        short.append(min(pair))
    return max(long)*max(short)