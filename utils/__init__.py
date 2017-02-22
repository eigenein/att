#!/usr/bin/env python3

from typing import List, Tuple

SOLID_ALPHA = 0xFF000000


def print_theme(colors: List[Tuple[str, int]]):
    """
    Prints out a theme.
    """
    for color_name, color in colors:
        print(f"{color_name}=#{color:08X}")
