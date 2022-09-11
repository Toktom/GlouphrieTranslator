# -*- coding: utf-8 -*-
"""
An example script to extract the Infobox Familiar from a RSW page.
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
# Import the necessary modules
from GlouphrieTranslator import (
    get_rsw,
    get_infobox_familiar,
    get_zearg_templates,
    get_navboxes,
    get_databox_summoning_pouch,
    get_databox_summoning_scroll,
)

# Get the page and check if it exists
page, exists = get_rsw("Hellhound (familiar)")
if exists:
    # Get the Infobox Familiar
    familiar = get_infobox_familiar(page)
    # Get databoxes on the page
    pouch = get_databox_summoning_pouch(page)
    scroll = get_databox_summoning_scroll(page)
    # Get all the zero-argument templates
    zeargt = get_zearg_templates(page)
    # Get all navboxes
    navboxes = get_navboxes(page)
    # Write the infobox item to a file
    with open("familiar_test.txt", "w", encoding="utf-8") as f:
        f.write(familiar + "\n\n")
        f.write(pouch + "\n\n")
        f.write(scroll + "\n")
        f.write(zeargt)
        f.write(navboxes)
        f.close()
