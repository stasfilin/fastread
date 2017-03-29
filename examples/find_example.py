import timeit

from fastread import Fastread

def main():
    ff = Fastread('big.txt')
    lines = ff.lines()

    total = 0

    for x in lines:
        total += 1

    return total

if __name__ == "__main__":
    total = main()
    timer = timeit.timeit("main()",
                          setup="from __main__ import main",
                          number=1)
    print('Read time: ', timer, '| Total lines: ', total)
