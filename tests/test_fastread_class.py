import pytest
import os

from fastread import Fastread

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def count_total_lines(lines):
    total = 0

    for l in lines:
        total += 1
    return total

def test_fastread_load_file():

    ff = Fastread(BASE_DIR+'/tests/data/test_data.txt')
    total = count_total_lines(ff.lines())
    assert total == 128457

def test_fastread_find_word():

    ff = Fastread(BASE_DIR+'/tests/data/test_data.txt')

    total = count_total_lines(ff.find('big'))

    assert total == 94
