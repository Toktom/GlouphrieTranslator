
# -*- coding: utf-8 -*-
"""
An example script to check the pages within a navbox (if they exist, have the
navbox in-it, get the rsw equivalent page).
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
# Import the necessary modules
from GlouphrieTranslator import (
    get_ptbr,
    get_template_by_name,
)
import pandas as pd
import re

nav_artifacts, exists = get_ptbr("Predefinição:Artefatos")
navbox = get_template_by_name(nav_artifacts, "Navbox")

plinks = re.findall(r"\{\{plink\|(.*?)\}\}", str(navbox))
suplinks = re.findall(r" <sup>\(\[\[(.*?)\|", str(navbox))
suplinks_extra = re.findall(r"\{\{\*\}\} \[\[(.*?)\]\]", str(navbox))
for i in range(0, len(suplinks_extra)):
    try:
        spe = suplinks_extra[i]
        e = re.findall(r"\|.*", spe)[0]
        suplinks_extra[i] = spe.replace(str(e), "")
    except:
        pass

df = pd.DataFrame(columns=["Page", "Exists", "Navbox"])

for pl in plinks:
    p, exists2 = get_ptbr(pl)
    art = get_template_by_name(p, "Artefatos")
    # add to data frame
    if art != None:
        df = df.append(
            {
                "Page": pl,
                "Exists": exists2,
                "Navbox": True,
            },
            ignore_index=True,
        )

for pl in suplinks:
    p, exists2 = get_ptbr(pl)
    art = get_template_by_name(p, "Artefatos")
    # add to data frame
    if art != None:
        df = df.append(
            {
                "Page": pl,
                "Exists": exists2,
                "Navbox": True,
            },
            ignore_index=True,
        )

for pl in suplinks_extra:
    p, exists2 = get_ptbr(pl)
    art = get_template_by_name(p, "Artefatos")
    # add to data frame
    if art != None:
        df = df.append(
            {
                "Page": pl,
                "Exists": exists2,
                "Navbox": True,
            },
            ignore_index=True,
        )

#write to excel df
df.to_excel("artifacts.xlsx")