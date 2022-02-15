#!/usr/bin/env python3

"""
This file demonstrates CodeQL pointing out a dict is unhashable, when it's inconsequential.
"""

def get_func(dictobj, *names):
    func_dict = dictobj
    for name in names:
        func_dict = func_dict[name]
    if not isinstance(func_dict, dict):
        raise TypeError(f"{name} is not a dictionary {func_dict!r}")
    return resolve_func(func_dict, name)
