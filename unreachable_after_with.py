#!/usr/bin/env python3

"""
This file demonstrates that code inside a `with` block may not be executed, and flow can continue after the end of the block.
"""

from contextlib import suppress


with suppress(ValueError):
  raise ValueError("You knew this would happen")
  
print("but here we are")
