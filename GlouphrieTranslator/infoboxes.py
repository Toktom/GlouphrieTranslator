# -*- coding: utf-8 -*-
"""
Infoboxes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
from .classes import InfoboxParameters
from .general import jsons_path

# Defines the Infobox Item
InfoboxItem = InfoboxParameters(
    "Infobox objeto", "Infobox Item", jsons_path + "item.json"
)
