# -*- coding: utf-8 -*-
"""
An example script to extract the infobox item from a RSW page.
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
# Import the necessary modules
from GlouphrieTranslator import (
    get_rsw,
    get_infobox_monster,
    get_zearg_templates,
    get_navboxes,
)

# Get the page and check if it exists
page, exists = get_rsw("K'ril Tsutsaroth")
if exists:
    # Get the infobox item
    item = get_infobox_monster(page)
    # Get all the zero-argument templates
    zeargt = get_zearg_templates(page)
    # Get all navboxes
    navboxes = get_navboxes(page)
    # Write the infobox item to a file
    with open("Tsutsaroth_test.txt", "w", encoding="utf-8") as f:
        f.write(item)
        f.write(zeargt)
        f.write(navboxes)
        f.close()
