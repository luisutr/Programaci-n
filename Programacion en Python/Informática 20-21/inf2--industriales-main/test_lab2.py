import pytest
import lab2 as l

def test_get_bb():
    run_tests('get_bb')

def test_draw_rect():
    run_tests('draw_rect')

def test_hl_rect():
    run_tests('hl_rect')

def test_find_bb():
    run_tests('find_bb')

def test_autocrop():
    run_tests('autocrop', run_autocrop)

def test_strel():
    run_tests('strel')

def test_imerode():
    run_tests('imerode')

def test_imdilate():
    run_tests('imdilate')

def test_get_mask():
    run_tests('get_mask')

def test_hl_objects():
    run_tests('hl_objects')

def test_autotransp():
    run_tests('autotransp')

import pickle
import urllib.request
from urllib.error import HTTPError
from imageio import imread, imwrite
import numpy as np

def run_tests(s, func = None):
    print(f'Getting tests {s}')
    try:
        uri = f'https://uclm-eiia-to.github.io/informatica/lab2/{s}.pickle'
        fp = urllib.request.urlopen(uri)
        tests = pickle.loads(fp.read())
        print(f'Got tests: {tests}')
    except HTTPError as e:
        print(f'Error obteniendo {uri}')
        raise e
    if func is None:
        func = getattr(l, s)
    for t in tests:
        run_test(t, func)

def run_test(s, func):
    print(f'Running {s}')
    try:
        uri = f'https://uclm-eiia-to.github.io/informatica/lab2/{s}.pickle'
        fp = urllib.request.urlopen(uri)
        args, expected = pickle.loads(fp.read())
    except HTTPError as e:
        print(f'Error obteniendo {uri}')
        raise e
    result = expected == func(*args)
    assert result if np.isscalar(result) else result.all()

def run_autocrop(ruta):
    uri = f'https://uclm-eiia-to.github.io/informatica/lab2/{ruta}'
    fp = urllib.request.urlopen(uri)
    local = f'{ruta}'
    with open(local, 'wb') as out:
        out.write(fp.read())
    l.autocrop(local)
    return imread(local)
    
