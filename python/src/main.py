#!/usr/bin/env python
from numpydoc.docscrape import NumpyDocString
from numpydoc.docscrape import FunctionDoc
from copy import copy


class Photo:
    """
    Array with associated photographic information.

    Parameters
    ----------
    x : type
        Description of parameter `x`.
    y
        Description of parameter `y` (with type not specified)

    Attributes
    ----------
    exposure : float
        Exposure in seconds.

    Methods
    -------
    colorspace(c='rgb')
        Represent the photo in the given colorspace.
    gamma(n=1.0)
        Change the photo's gamma exposure.

    """


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


def merge_parameters(existing: list, new: list) -> list:
    """Merge the sections of two docstrings."""
    result = []
    # We'll check all new parameters.
    for i, param in enumerate(new):
        # If there is a non-empty description, we'll consider it an updated parameter
        # and remove it from existing.
        # If empty, we'll continue to use the existing description.
        if param.desc != []:
            # existing = [e for e in existing if e.name != param.name]
            result.append(param) # The parameter is in the correct position.
        else:
            # In this case we need to find the corresponding parameter in existing.
            for existing_param in existing:
                if existing_param.name == param.name:
                    result.append(existing_param)
    return result


def merge_summary(existing: str, new: str) -> str:
    """Merge the summary section.

    Return the new summary if it exists, because that means it was updated.

    Parameters
    ----------
    existing : str
        The existing summary
    new : str
        The new summary

    Returns
    -------
    str
        The updated summary

    Examples
    --------
    FIXME: Add docs.

    """
    return new if new != "" else existing


def main():
    """Quiet."""
    # doc = NumpyDocString(Photo.__doc__)
    # print(doc["Summary"])
    # print(doc["Parameters"])
    # print(doc["Attributes"])
    # print(doc["Methods"])

    doc = FunctionDoc(foobar)
    doc2 = FunctionDoc(foobar2)
    doc3 = FunctionDoc(foobar3)
    merged = merge_parameters(doc["Parameters"], doc2["Parameters"])
    assert merged == doc3["Parameters"]
    print(doc["Parameters"])


if __name__ == "__main__":
    main()
