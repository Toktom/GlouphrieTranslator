# -*- coding: utf-8 -*-
"""
Functions file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
import mwparserfromhell as mw
import pywikibot as pwb
import re


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


def retrieve_parameters(t) -> list:
    """
    Returns the parameters of the template with the name and versioning
        (if it's present).

    Parameters:
        t (mwparserfromhell.nodes.Template): The template to search the parameters.

    Returns:
        list: The parameters of the template.
    """
    parameters = []
    for param in t.params:
        # splits the parameter from it's value
        param = param.replace("\n", "").split(" =")
        # if number with 2 digits in param[0]
        if re.search(r"\d{2}", param[0]):
            # get number in param[0]
            param_number = re.search(r"\d{2}", param[0]).group()
            parameters.append([param[0].replace(param_number, ""), param_number])
        elif re.search(r"\d", param[0]):
            param_number = re.search(r"\d", param[0]).group()
            parameters.append([param[0].replace(param_number, ""), param_number])
        else:
            parameters.append([param[0], "0"])

    return parameters
