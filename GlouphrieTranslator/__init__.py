# -*- coding: utf-8 -*-
"""
Module initialization file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
from .classes import InfoboxParameters
from .functions import get_infobox_item, get_ptbr, get_rsw
from .general import (
    get_item_br_name_by_en,
    get_item_en_name_by_br,
    get_item_names_by_id,
)
from .infoboxes import InfoboxItem

__all__ = [
    "InfoboxItemParser",
    "InfoboxParameters",
    "get_infobox_item",
    "get_ptbr",
    "get_rsw",
    "get_item_names_by_id",
    "get_item_br_name_by_en",
    "get_item_en_name_by_br",
    "InfoboxItem",
]

__author__ = "Michael Markus Ackermann; João Pedro Droval"
__date__ = "02 August 2022"
__version__ = "0.0.5"
