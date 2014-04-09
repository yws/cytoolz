from cytoolz.utils import testmod

import cytoolz
import cytoolz.dicttoolz
import cytoolz.functoolz
import cytoolz.itertoolz
import cytoolz.recipes


# This currently doesn't work.  Use `cydoctest.py` instead.
def test_doctest():
    testmod(cytoolz)
    testmod(cytoolz.dicttoolz)
    testmod(cytoolz.functoolz)
    testmod(cytoolz.itertoolz)
    testmod(cytoolz.recipes)
