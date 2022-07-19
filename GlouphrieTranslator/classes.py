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
)


@dataclass
class Parameter:
    br: str
    en: str


@dataclass
class InfoboxParamParser(ABC):
    param: Parameter

    @abstractmethod
    def parse(self, param):
        pass


@dataclass
class InfoboxParameters:
    br: str
    en: str
    file: dict
    parameters: List[Parameter] = field(default_factory=list)

    def __post_init__(self):
        self._set_parameters()
        return None

    def _set_parameters(self):
        params = self.__infobox_from_json(self.file)

        for i in range(len(params[0])):
            self.parameters.append(Parameter(params[0][i], params[1][i]))
        return None

    def get_parameter(self, param, lang="en"):
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
    def __infobox_from_json(fname):
        with open(fname, "r", encoding="utf-8") as json_file:
            params = json.load(json_file)
            json_file.close()

        return [list(params.keys()), list(params.values())]


@dataclass
class InfoboxItemParser(InfoboxParamParser):
    def parse(self, param):
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
                parsed = f"<!--Untranslatable:{parsed}-->\n"
        except:
            print("Failed to parse the parameter: ", self.param.en)
            parsed = str(param).replace("\n", "")
            parsed = f"<!--Failed:{parsed}-->\n"

        return f"|{self.param.br} = {parsed}"
