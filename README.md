# Fastread
_Fastread is a library for read big files_

## How to install and update

Install latest stable version or update current from pip.

```python
pip install -U fastread
```

## Basic Usage

Here's a simple example.

```python
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

#RESULT
# Read time:  0.029999009988387115 | Total lines:  128457
```

## Reference

| Setup   | Command                | Notes |
| ------- | ---------------------- | ----- |
| install | `pip install fastread` |       |

