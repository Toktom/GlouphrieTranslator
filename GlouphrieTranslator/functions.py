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


def get_ptbr(title: str):
    """
    Returns the PT-BR page.

    Parameters:
        title (str): The title of the page.

    Returns:
        str: The wikicode parsed of the pt-br page.
        bool: True if the page exists, False otherwise.
    """
    site = pwb.Site()
    page = pwb.Page(site, title)
    text = page.get()
    if_exist = page.exists()
    return mw.parse(text), if_exist


def get_rsw(title):
    """
    Returns the English page.

    Parameters:
        title (str): The title of the page.

    Returns:
        str: The wikicode parsed of the english page.
        bool: True if the page exists, False otherwise.
    """
    site = pwb.Site("en-gb", "rsw")
    page = pwb.Page(site, title)
    text = page.get()
    if_exist = page.exists()
    return mw.parse(text), if_exist


def get_template_by_name(page, name: str):
    """
    Returns the template by its name.

    Parameters:
        page: The page to search the template.
        name (str): The name of the template.

    Returns:
        The template.
    """
    templates = page.filter_templates()
    try:
        for template in templates:
            if template.name.matches(name):
                return template
    except:
        return None


def get_infobox_item(page) -> str:
    """
    Returns the translated infobox item.

    Parameters:
        page: The page to search the infobox item.

    Returns:
        str: The infobox item.
    """
    try:
        out = f"{{{{{InfoboxItem.br}\n"

        t = get_template_by_name(page, InfoboxItem.en)

        for param in InfoboxItem.parameters:
            try:
                param_val = t.get(param.en).value
                Parser = InfoboxItemParser(param)
                out += Parser.parse(param_val)
            except Exception as e:
                print(f"Unable to retrieve '{e}' parameter.")

        out += f"}}}}"
        return out
    except:
        raise Exception("Error while parsing infobox item!")
