#!/usr/bin/env python3

from typing import List, Tuple

SOLID = 0xFF


def argb(rgb: int, alpha: int) -> int:
    """
    Takes RGB color value and alpha value and combines them into single integer.
    """
    assert 0x000000 <= rgb <= 0xFFFFFF
    assert 0 <= alpha <= 0xFF
    value = rgb | (alpha << 24)
    if value >= 0x80000000:
        value -= 0x100000000
    return value


def print_theme(colors: List[Tuple[str, int]]):
    """
    Prints out a theme.
    """
    for color_name, color in colors:
        print(f"{color_name}={color}")
