# -*- coding: utf-8 -*-
"""
Setup file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""

from setuptools import setup

settings = {
    "name": "GlouphrieTranslator",
    "version": "0.0.1",
    "description": "GlouphrieTranslator (or GT) is an integration of MWParserFromHell and PyWikiBot. This tool allows PT-BR Runescape Wiki editors to increase their editing speed when translating the pages from RSW. The key feature of the tool is the auto-template translator.",
    "url": "https://github.com/Toktom/GlouphrieTranslator",
    "author": "Michael Markus Ackermann",
    "license": "Apache License 2.0",
    "install_requires": [
        "mwparserfromhell>=0.6.3",
        "pywikibot>=6.5.0",
    ],
    "packages": ["GlouphrieTranslator", "GlouphrieTranslator.jsons", "GlouphrieTranslator.txts"],
}

setup(**settings)