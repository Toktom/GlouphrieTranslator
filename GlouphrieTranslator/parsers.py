# -*- coding: utf-8 -*-
"""
Parsers file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
import json

from .general import (
    jsons_path,
    months_br,
    months_en,
    get_actions_lists,
    get_item_br_name_alias,
)


def parse_int(param: any) -> str:
    param = str(param)
    if isinstance(int(param), int):
        return param
    else:
        pass
    return param


def parse_float(param: any) -> str:
    param = str(param)
    if isinstance(float(param), float):
        return param.replace(".", ",")
    else:
        pass
    return param.replace(".", ",")


def parse_yes_no(param: any) -> str:
    param = str(param).lower()
    if "yes" in param:
        return "Sim\n"
    elif "no" in param:
        return "Não\n"
    else:
        parsed = str(param).replace("\n", "")
        return f"<!--Failed: {parsed}-->\n"


def parse_disassembly(param: any) -> str:
    param = str(param).lower()
    if "restricted" in param:
        return "restrito\n"
    elif "n/a" in param:
        return "N/A\n"
    else:
        return parse_yes_no(param)


def parse_kept(param: any) -> str:
    param = str(param).lower()
    if "reclaimable" in param:
        return "recuperável\n"
    elif "never" in param:
        return "nunca\n"
    elif "always" in param:
        return "sempre\n"
    elif "alwaysinclwild" in param:
        return "semprewild\n"
    elif "dropped" in param:
        return "largado\n"
    elif "safe" in param:
        return "seguro\n"
    else:
        parsed = str(param).replace("\n", "")
        return f"<!--Failed: {parsed}-->\n"


def parse_date(param: any) -> str:
    param = str(param)
    if any(month in param for month in months_en):
        p = param.replace("[[", "").replace("]]", "")
        elements = p.split(" ")
        elements = [e for e in elements if e != ""]
        month = elements[1]
        month_index = months_en.index(month)
        month = months_br[month_index]
        return (
            "{{Data|"
            + str(int(elements[0]))
            + "|"
            + month.lower()
            + "|"
            + str(int(elements[2]))
            + "}}\n"
        )
    else:
        parsed = str(param).replace("\n", "")
        return f"<!--Failed: {parsed}-->\n"


def parse_quest(param: any) -> str:
    param = str(param).replace("[[", "").replace("]]", "").replace("\n", "")
    param = [x for x in param.split(" ") if x != ""]
    param = " ".join(param).lower()
    with open(f"{jsons_path}quests_list.json", "r", encoding="utf-8") as f:
        jd1 = json.load(f)
        f.close()
    quests = [list(jd1.keys()), list(jd1.values())]

    with open(f"{jsons_path}miniquests_list.json", "r", encoding="utf-8") as f:
        jd2 = json.load(f)
        f.close()
    miniquests = [list(jd2.keys()), list(jd2.values())]

    en_list = [str(x).lower() for x in quests[1]]
    en_mini_list = [str(x).lower() for x in miniquests[1]]

    if (len(param) <= 5) and ("no" in param):
        return "Não\n"
    elif param in en_list:
        index = en_list.index(param)
        value = quests[0][index]
        return f"{{{{Missão|{value}}}}}\n"
    elif param in en_mini_list:
        index = en_mini_list.index(param)
        value = miniquests[0][index]
        return f"{{{{Missão|{value}}}}}\n"
    else:
        return "{{Desconhecido}}\n"


def parse_restriction(param: any) -> str:
    param = str(param).lower()
    if "surface" in param:
        return "superfície\n"
    elif "quest" in param:
        return "missão\n"
    elif any(["minigame", "activity"]) in param:
        return "minijogo\n"
    elif (
        any(["dungeon", "dungeoneering", "dg", "daemonheim", "kalaboss"])
        in param
    ):
        return "dungeon\n"
    elif any(["removed", "beta", "gone"]) in param:
        return "removido\n"
    elif any(["limited", "'time limited"]) in param:
        return "limitado\n"
    elif any(["th", "sof", "treasure hunter", "squeal of fortune"]) in param:
        return "arca do tesouro\n"
    elif "cache" in param:
        return "cache\n"
    else:
        return param


def parse_item_name(param):
    param = str(param)
    param = " ".join([x for x in param.replace("\n", "").split(" ") if x != ""])
    br_name = get_item_br_name_alias(param)
    if br_name:
        return f"|nome = {br_name}\n|inglês = {param}\n|imagem = [[Ficheiro:{br_name}.png]]\n"
    else:
        param = f"<!--{param}-->"
        return f"|nome = {param}\n|inglês = {param}\n|imagem = {param}\n"


def parse_destroy(param):
    param = str(param).lower()
    if "drop" in param and len(param) <= 7:
        return "Largar\n"
    else:
        parsed = str(param).replace("\n", "")
        return f"<!--Untranslatable: {parsed}-->\n"


def parse_actions(param):
    param = str(param).lower()
    params = [x.replace(",", "") for x in param.replace("\n", "").split(",") if x != ""]
    params = [x.rstrip().lstrip()for x in params]
    actions_list = get_actions_lists()
    lowered_actions = [x.lower() for x in actions_list[0]]
    actions = []
    for p in params:
        if p in lowered_actions:
            idx = lowered_actions.index(p)
            actions.append(actions_list[1][idx])
        else:
            actions.append(f"<!--Unrecognized action: {p}-->")
    return ", ".join(actions) + "\n"
