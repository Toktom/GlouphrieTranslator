# -*- coding: utf-8 -*-
"""
Functions file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
import mwparserfromhell as mw
import pywikibot as pwb

from .classes import InfoboxItemParser
from .infoboxes import InfoboxItem


def get_ptbr(title):
    site = pwb.Site()
    page = pwb.Page(site, title)
    text = page.get()
    if_exist = page.exists()
    return mw.parse(text), if_exist


def get_rsw(title):
    site = pwb.Site("en-gb", "rsw")
    page = pwb.Page(site, title)
    text = page.get()
    if_exist = page.exists()
    return mw.parse(text), if_exist


def get_template_by_name(page, name):
    templates = page.filter_templates()
    try:
        for template in templates:
            if template.name.matches(name):
                return template
    except:
        return None


def get_infobox_item(page):
    try:
        out = f"{{{{{InfoboxItem.br}\n"

        t = get_template_by_name(page, InfoboxItem.en)

        for param in InfoboxItem.parameters:
            try:
                param_val = t.get(param.en).value
                Parser = InfoboxItemParser(param)
                out += Parser.parse(param_val)
            except:
                pass

        out += f"}}}}"
        return out
    except:
        raise Exception("Error while parsing infobox item!")