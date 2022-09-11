# -*- coding: utf-8 -*-
"""
Module initialization file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
from .classes import InfoboxParameters
from .databoxes import (
    DataboxSummoningPouch,
    DataboxSummoningScroll,
    get_databox_summoning_pouch,
    get_databox_summoning_scroll,
)
from .functions import get_ptbr, get_rsw
from .general import (
    get_item_br_name_by_en,
    get_item_en_name_by_br,
    get_item_names_by_id,
)
from .infoboxes import (
    InfoboxFamiliar,
    InfoboxItem,
    InfoboxMonster,
    get_infobox_familiar,
    get_infobox_item,
    get_infobox_monster,
)
from .templates import get_navboxes, get_zearg_templates

__all__ = [
    "InfoboxItemParser",
    "InfoboxParameters",
    "get_infobox_item",
    "get_infobox_monster",
    "get_infobox_familiar",
    "get_databox_summoning_pouch",
    "get_databox_summoning_scroll",
    "get_ptbr",
    "get_rsw",
    "get_item_names_by_id",
    "get_item_br_name_by_en",
    "get_item_en_name_by_br",
    "InfoboxItem",
    "InfoboxMonster",
    "InfoboxFamiliar",
    "DataboxSummoningPouch",
    "DataboxSummoningScroll",
    "get_zearg_templates",
    "get_navboxes",
]

__author__ = "Michael Markus Ackermann; João Pedro Droval"
__date__ = "11 September 2022"
__version__ = "0.0.9"
