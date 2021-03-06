# MIT License

# Copyright (c) 2016 Alexis Bekhdadi (midoriiro) <contact@smartsoftwa.re>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

import pytest

from subways.utils import PartialDictComparer, AttributeDict


class A:
    def __init__(self):
        self.i = 0
        self.j = 1
        self.k = 2


class B(AttributeDict):
    pass


def test_partial_comparer():
    d = {
        'i': 0,
        'j': 1,
        'k': 2
    }

    assert PartialDictComparer(A()) == d

    del d['i']

    assert PartialDictComparer(A()) == d

    d['i'] = 666
    d['j'] = 3

    assert PartialDictComparer(A()) == d

    d['k'] = 5

    assert PartialDictComparer(A()) != d

    assert PartialDictComparer(A()) != {}

    d = {
        'x': 0,
        'y': 1,
        'z': 2
    }

    assert PartialDictComparer(A()) != d


def test_attributes_dict():
    b = B()
    b.i = 0
    b.j = 2
    b.k = 3

    assert b.i == 0
    assert b.j == 2
    assert b.k != 4

    assert b['i'] == 0
    assert b['j'] == 2
    assert b['k'] != 4

    for key in b.keys():
        if key == 'i':
            assert b[key] == 0
        elif key == 'j':
            assert b[key] == 2
        elif key == 'k':
            assert b[key] != 4
        else:
            assert b[key]
