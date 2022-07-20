# -*- coding: utf-8 -*-
"""
Setup file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""

from setuptools import setup

settings = {
    "name": "GlouphrieTranslator",
    "version": "0.0.2b",
    "description": "GlouphrieTranslator (or GT) is an integration of MWParserFromHell and PyWikiBot. This tool allows PT-BR Runescape Wiki editors to increase their editing speed when translating the pages from RSW. The key feature of the tool is the auto-template translator.",
    "url": "https://github.com/Toktom/GlouphrieTranslator",
    "author": "Michael Markus Ackermann",
    "license": "Apache License 2.0",
    "python_requires" : "<=3.8.10",
    "install_requires": [
        "mwparserfromhell>=0.6.3",
        "pywikibot>=6.5.0",
    ],
    "packages": ["GlouphrieTranslator"],
    "include_package_data": True,
    "package_data": {
        "GlouphrieTranslator": ["jsons/*.json", "txts/*.txt"],
    },
}


setup(**settings)
