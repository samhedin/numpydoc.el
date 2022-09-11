#!/usr/bin/env python
from numpydoc.docscrape import FunctionDoc
from src.main import merge_parameters, merge


def foobar(a, b):
    """
    Something something.

    Parameters
    ----------
    a : int, default: 5
         Does something cool
    b : str
         Wow
    """
    return a + b


def foobar2(a, b):
    """A new description

    Parameters
    ----------
    a : int
        Does something cool
    b :

    Examples
    --------
    FIXME: Add docs.

    """
    return a + b


def foobar3(a, b):
    """A new description

    Parameters
    ----------
    a : int
        Does something cool
    b : str
        Wow

    Examples
    --------
    FIXME: Add docs.

    """


def test_merge():
    doc = FunctionDoc(foobar)
    doc2 = FunctionDoc(foobar2)
    doc3 = FunctionDoc(foobar3)
    merged_parameters = merge_parameters(doc["Parameters"], doc2["Parameters"])
    assert merged_parameters == doc3["Parameters"]

    assert doc3 == merge(doc, doc2)
