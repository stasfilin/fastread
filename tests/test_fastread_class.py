import os

from fastread import Fastread

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def count_total_lines(lines):
    total = 0

    for l in lines:
        total += 1
    return total


def test_fastread_lines():

    ff = Fastread(BASE_DIR+'/tests/data/test_data.txt')
    total = count_total_lines(ff.lines())
    assert total == 128457


def test_fastread_find_word():

    ff = Fastread(BASE_DIR+'/tests/data/test_data.txt')
    total = count_total_lines(ff.find('big'))
    assert total == 94


def test_load_invalid_file():

        ff = Fastread('invalid_file.txt')
        try:
            count_total_lines(ff.lines())
        except FileNotFoundError as e:
            assert type(e) == FileNotFoundError


def test_fastread_lines_with_sep():

    ff = Fastread(BASE_DIR+'/tests/data/test_data.txt')
    lines = ff.lines(sep=',')
    assert len(list(lines)[1232]) == 2


def test_fastread_get_row():

    ff = Fastread(BASE_DIR+'/tests/data/test_data.txt')
    row = ff.row(1)
    assert row == "by Sir Arthur Conan Doyle\n"
