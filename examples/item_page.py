# -*- coding: utf-8 -*-
"""
An example script to extract the infobox item from a RSW page.
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
# Import the necessary modules
from GlouphrieTranslator import (
    get_rsw,
    get_infobox_item,
    get_zearg_templates,
    get_navboxes,
)

# Get the page and check if it exists
page, exists = get_rsw("Zaros godsword")
if exists:
    # Get the infobox item
    item = get_infobox_item(page)
    # Get all the zero-argument templates
    zeargt = get_zearg_templates(page)
    # Get all navboxes
    navboxes = get_navboxes(page)
    # Write the infobox item to a file
    with open("zgs_test.txt", "w", encoding="utf-8") as f:
        f.write(item)
        f.write(zeargt)
        f.write(navboxes)
        f.close()
