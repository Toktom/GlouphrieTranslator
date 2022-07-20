# -*- coding: utf-8 -*-
"""
Module initialization file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
from .classes import InfoboxItemParser, InfoboxParameters
from .functions import get_infobox_item, get_ptbr, get_rsw
from .general import (
    get_item_br_name_alias,
    get_item_en_name_alias,
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
    "get_item_br_name_alias",
    "get_item_en_name_alias",
    "InfoboxItem",
]

__author__ = "Michael Markus Ackermann"
__date__ = "20 July 2022"
__version__ = "0.0.3"
