# -*- coding: utf-8 -*-
"""
This family file was auto-generated by generate_family_file.py script.

Configuration parameters:
  url = https://runescape.wiki
  name = rsw

Please do not commit this to the Git repository!
"""
from __future__ import absolute_import, division, unicode_literals

from pywikibot import family
from pywikibot.tools import deprecated


class Family(family.Family):

    name = "rsw"
    langs = {
        "en-gb": "runescape.wiki",
        "pt-br": "pt.runescape.wiki",
    }

    def scriptpath(self, code):
        return {
            "en-gb": "",
            "pt-br": "",
        }[code]

    @deprecated("APISite.version()")
    def version(self, code):
        return {
            "en-gb": "1.31.9",
            "pt-br": "1.31.9",
        }[code]

    def protocol(self, code):
        return {
            "en-gb": "https",
            "pt-br": "https",
        }[code]