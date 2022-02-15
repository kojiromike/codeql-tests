#!/usr/bin/env python3

"""
This file demonstrates that code inside a `with` block may not be executed, and flow can continue after the end of the block.
"""

from contextlib import suppress


def raiser() -> NoReturn:
  raise ValueError("You knew this would happen")


def main() -> str:
  with suppress(ValueError):
    return raiser()
  
  return "but here we are"

print(main())
