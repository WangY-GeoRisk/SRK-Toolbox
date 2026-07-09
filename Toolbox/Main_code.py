"""
# -*- coding: utf-8 -*-
# @Author: cONg
# @Time 20260324
"""

import os
import sys
import arcpy

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
if _THIS_DIR not in sys.path:
    sys.path.insert(0, _THIS_DIR)

try:
    import SRK_Tool as SRKT
except ImportError:
    raise ImportError(
        "Failed to import SR_Kriging_Tool. "
        "Ensure SR_Kriging_Tool.pyc is in the same folder."
    )


def main():
    SRKT.run()


if __name__ == "__main__":
    main()
