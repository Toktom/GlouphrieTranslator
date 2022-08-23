# -*- coding: utf-8 -*-
"""
General templates

Includes:
-> navboxes; and
-> simple templates (templates with one line or without more then 2 or 3 parameters).
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
from .general import get_zeargt_list, get_navboxes_list


def get_zearg_templates(page):
    """
    Returns every zero-argument (zearg) template in the page.

    Parameters:
        page: The page to search for zearg templates.

    Returns:
        str: The zearg templates.
    """
    zearg_list = get_zeargt_list()
    lowered_zearg = [x.lower() for x in zearg_list[0]]
    try:
        output = "\n<!-- zearg templates -->"
        for template in page.filter_templates():
            if template.name.lower() in lowered_zearg:
                idx = lowered_zearg.index(template.name.lower())
                output += f"\n{{{{{zearg_list[1][idx]}}}}}"
        if len(output) == 25:
            print("No zearg template has been translated!")
            return ""
        else:
            return output
    except Exception as e:
        raise Exception("Error while translating zero-argument templates!")

def get_navboxes(page):
    """
    Returns every navbox in the page.

    Parameters:
        page: The page to search for navboxes.

    Returns:
        str: The navboxes.
    """
    nav_list = get_navboxes_list()
    lowered_navs = [x.lower() for x in nav_list[0]]
    try:
        output = "\n<!-- navboxes -->"
        for template in page.filter_templates():
            if template.name.lower() in lowered_navs:
                idx = lowered_navs.index(template.name.lower())
                output += f"\n{{{{{nav_list[1][idx]}}}}}"
        if len(output) == 18:
            print("No navbox has been translated!")
            return ""
        else:
            return output
    except Exception as e:
        raise Exception("Error while translating navboxes!")