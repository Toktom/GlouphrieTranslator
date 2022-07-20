# -*- coding: utf-8 -*-
"""
Classes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List

from .parsers import (
    parse_actions,
    parse_date,
    parse_destroy,
    parse_disassembly,
    parse_float,
    parse_int,
    parse_item_name,
    parse_kept,
    parse_quest,
    parse_restriction,
    parse_yes_no,
    parse_exchange,
)


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
class InfoboxParamParser(ABC):
    """
    A abstract class that represents a parser for a parameter.

    Attributes:
        parameter (Parameter): The parameter to parse.

    Methods:
        parse(self, param: str) -> str:
            Parses the parameter.
    """

    param: Parameter

    @abstractmethod
    def parse(self, param: str):
        """
        Parses the parameter.

        Parameters:
            param (str): The parameter to parse.

        Returns:
            str: The parsed parameter.
        """
        pass


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


@dataclass
class InfoboxItemParser(InfoboxParamParser):
    """
    A class that represents a parser for the Infobox Item.

    Attributes:
        parameter (Parameter): The parameter to parse.

    Methods:
        parse(self, param: str) -> str:
            Parses the parameter.
    """

    def parse(self, param: str)-> str:
        """
        Parses the parameter.

        Parameters:
            param (str): The parameter to parse.

        Returns:
            str: The parsed parameter.
        """
        try:
            if self.param.en == "name":
                return parse_item_name(param)
            elif self.param.en == "weight":
                parsed = parse_float(param)
            elif self.param.en == "quest":
                parsed = parse_quest(param)
            elif self.param.en == "disassembly":
                parsed = parse_disassembly(param)
            elif self.param.en in ["value"]:
                parsed = parse_int(param)
            elif self.param.en == "exchange":
                parsed = parse_exchange(param)
            elif self.param.en == "id":
                if isinstance(param, list):
                    parsed = [parse_int(x) for x in param]
                    parsed = ", ".join(parsed)
                else:
                    parsed = parse_int(param)
            elif self.param.en in ["release", "removal"]:
                parsed = parse_date(param)
            elif self.param.en == "kept":
                parsed = parse_kept(param)
            elif self.param.en == "restriction":
                parsed = parse_restriction(param)
            elif self.param.en == "destroy":
                parsed = parse_destroy(param)
            elif self.param.en in [
                "actions",
                "actions_ground",
                "actions_equipped",
                "actions_bank",
                "actions_currency_pouch",
            ]:
                parsed = parse_actions(param)
            elif self.param.en in [
                "stacksinbank",
                "stackable",
                "equipable",
                "tradeable",
                "members",
                "alchable",
            ]:
                parsed = parse_yes_no(param)
            else:
                parsed = str(param).replace("\n", "")
                parsed = f"{parsed} <!--Untranslatable-->\n"
        except:
            print("Failed to parse the parameter: ", self.param.en)
            parsed = str(param).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        return f"|{self.param.br} = {parsed}"
