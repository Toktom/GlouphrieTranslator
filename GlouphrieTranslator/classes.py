# -*- coding: utf-8 -*-
"""
Classes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
import json
from dataclasses import dataclass, field
from typing import List

@dataclass
class Parameter:
    """
    A class that represents a parameter.

    Attributes:
        br (str): The pt-br name of the parameter.
        en (str): The english name of the parameter.
    """

    br: str
    en: str

@dataclass
class InfoboxParameters:
    """
    A class to retrieve the infobox parameters from a json file and hold them.

    Attributes:
        br (str): The pt-br name of the infobox.
        en (str): The english name of the infobox.
        file (str): The file to retrieve the parameters from.
        parameters (List[Parameter]): The parameters.
    """

    br: str
    en: str
    file: dict
    parameters: List[Parameter] = field(default_factory=list)

    def __post_init__(self):
        """
        Post initializes the parameters.

        Returns:
            None
        """
        self._set_parameters()
        return None

    def _set_parameters(self):
        """
        Sets the parameters.

        Returns:
            None
        """
        params = self.__infobox_from_json(self.file)

        for i in range(len(params[0])):
            self.parameters.append(Parameter(params[0][i], params[1][i]))
        return None

    def get_parameter(self, param: str, lang: str = "en") -> str:
        """
        Returns the parameter by its name.

        Parameters:
            param (str): The name of the parameter.
            lang (str): The language of the parameter.

        Returns:
            str: The parameter.
        """
        if len(self.parameters) != 0:
            for p in self.parameters:
                if lang == "en":
                    if p.en == param:
                        return p
                elif lang == "br":
                    if p.br == param:
                        return p
        else:
            raise Exception("No parameters found!")
        return None

    @staticmethod
    def __infobox_from_json(fname: str) -> list:
        """
        Returns the infobox parameters from a json file.

        Parameters:
            fname (str): The name of the json file.

        Returns:
            list: A list with the br and english names of the parameters.
        """
        with open(fname, "r", encoding="utf-8") as json_file:
            params = json.load(json_file)
            json_file.close()

        return [list(params.keys()), list(params.values())]