# -*- coding: UTF-8 -*-

# Import from standard library
import os
import build_your_toolbox
import pandas as pd
# Import from our lib
from build_your_toolbox.lib import *
import pytest

def test_multiplication():
    assert multiplication(2,4) == 8

def test_division():
    assert division(8,2) == 4

def test_addition():
    assert addition(2,4) == 6

def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(build_your_toolbox.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)
