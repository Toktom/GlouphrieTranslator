# -*- coding: utf-8 -*-
"""
An example script to extract the infobox item from a RSW page.
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
# Import the necessary modules
from GlouphrieTranslator import get_infobox_item, get_rsw

# Get the page and check if it exists
page, exists = get_rsw("Zaros godsword")
# Get the infobox item
pagina = get_infobox_item(page)

# Write the infobox item to a file
with open("zgs_ptbr.txt", "w", encoding="utf-8") as f:
    f.write(pagina)
    f.close()
