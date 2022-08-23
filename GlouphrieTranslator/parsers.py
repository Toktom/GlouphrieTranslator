# -*- coding: utf-8 -*-
"""
Parsers file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
import json
import requests
from lxml import html

from .general import (
    jsons_path,
    get_actions_lists,
    get_item_br_name_by_en,
)


def parse_int(param: any) -> str:
    """
    Parses parameter values to make shure that the expected param is an integer
    and returns it as a string.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The parsed parameter value.
    """
    param = str(param)
    if isinstance(int(param), int):
        return param
    else:
        return f"{param} <!--Failed-->\n"


def parse_float(param: any) -> str:
    """
    Parses parameter values to make shure that the expected param is a float and
    returns it as a string.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The parsed parameter value.
    """
    param = str(param)
    if isinstance(float(param), float):
        return param.replace(".", ",")
    else:
        return param.replace(".", ",") + " <!--Failed-->\n"


def parse_yes_no(param: any) -> str:
    """
    Parses parameter values to make shure that the expected param is a yes or no
    and returns it as a pt-br string.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The parsed parameter value.
    """
    param = str(param).lower()
    if "yes" in param:
        return "Sim\n"
    elif "no" in param:
        return "Não\n"
    else:
        parsed = str(param).replace("\n", "")
        return f"{parsed} <!--Failed-->\n"


def parse_disassembly(param: any) -> str:
    """
    Parses parameter values to make shure that the expected param is a supported
    disassembly value and returns the corresponding pt-br string.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The parsed parameter value.
    """
    param = str(param).lower()
    if "restricted" in param:
        return "restrito\n"
    elif "n/a" in param:
        return "N/A\n"
    else:
        return parse_yes_no(param)


def parse_kept(param: any) -> str:
    """
    Parses parameter values to make shure that the expected param is a supported
    kept value and returns the corresponding pt-br string.
    """
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
        return f"{parsed} <!--Failed-->\n"


def parse_date(param: any) -> str:
    """
    Parses parameter date value to create the date template in pt-br format.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The date template with the corresponding date.
    """
    param = str(param)
    with open(f"{jsons_path}months_names.json", "r", encoding="utf-8") as f:
        months = json.load(f)
        f.close()

    p = param.replace("[[", "").replace("]]", "")
    elements = p.split(" ")

    for item in elements:
        if item in months:
            # Converting to int removes the ocasional "\n".
            year = int(elements[elements.index(item) + 1])
            day = int(elements[elements.index(item) - 1])
            pt_br_month = months[item]
            return f"{{{{Data|{day}|{pt_br_month.lower()}|{year}}}}}\n"

    parsed = str(param).replace("\n", "")
    return f"{parsed} <!--Failed-->\n"


def parse_examine(param: any, id, name) -> str:
    name = str(name)
    page = html.fromstring(
        requests.get(
            f"https://secure.runescape.com/m=itemdb_rs/l=3/{name}/viewitem?obj={id}"
        ).content
    )

    try:
        examine = page.xpath('.//div[@class="content roughTop"]//div/p/text()')[0]
        return f"{examine}\n"
    except IndexError:
        param = str(param).replace("\n", "")
        return f"{param} <!--Untranslatable-->\n"


def parse_quest(param: any) -> str:
    """
    Parses parameter to check if is a quest or miniquest and returns the
    corresponding quest/miniquest template in the pt-br format.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The quest template with the corresponding quest or miniquest.
    """
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
        return f"{param} <!--Untranslatable-->\n"


def parse_restriction(param: any) -> str:
    """
    Parses parameter to check if is a restriction and returns the
    corresponding restriction value pt-br.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The restriction value pt-br.
    """
    param = str(param).lower()
    if "surface" in param:
        return "superfície\n"
    elif "quest" in param:
        return "missão\n"
    elif any(["minigame", "activity"]) in param:
        return "minijogo\n"
    elif any(["dungeon", "dungeoneering", "dg", "daemonheim", "kalaboss"]) in param:
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
        return f"{param} <!--Untranslatable-->\n"


def parse_version(param: any) -> str:
    """
    Parses parameter to check if is a version and to get it's respective
    pt-br equivalent.

    Parameters:
        param (any): The version parameter to be parsed.

    Returns:
        str: The version equivalent in pt-br.
    """
    param = str(param)
    param = param[1:] # The first char is always an empty space.
    param = param[:-1] # The last char is always a new line.

    return { "new":"Novo\n", "used":"Usado\n", "broken":"Quebrado\n" }.get(param)


def parse_item_name(param: any, num: int) -> str:
    """
    Parses parameter to check if is a item name and tries to get the item name
    in pt-br, then proceeds to get create the english and image parameters,
    based on the pt-br name.

    NOTE: This function is slow, do to the for inside the function that tries
    to get the pt-br name of the english item name.

    Parameters:
        param (any): The parameter value to be parsed;
        num (int): The number of the param's version.

    Returns:
        str: The parameters for name, image and english page name.
    """
    param = str(param)
    param = " ".join([x for x in param.replace("\n", "").split(" ") if x != ""])
    br_name = get_item_br_name_by_en(param)
    if int(num) == 0 or int(num) == 1:
        if br_name:
            return f"|nome = {br_name}\n|inglês = {param}\n|imagem = [[Arquivo:{br_name}.png]]\n"
        else:
            param = f"{param} <!--Untranslatable-->"
            return f"|nome = {param}\n|inglês = {param}\n|imagem = {param}\n"
    else:
        param = f"{param} <!--Untranslatable-->"
        return f"|nome{num} = {param}\n|inglês{num} = {param}\n|imagem{num} = {param}\n"



def parse_destroy(param: any) -> str:
    """
    Parses parameter to check if has the standard destroy value or a custom
    destroy message.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: "Largar" or the untranslated english message.
    """
    param = str(param).lower()
    if "drop" in param and len(param) <= 7:
        return "Largar\n"
    else:
        parsed = str(param).replace("\n", "")
        return f" {parsed} <!--Untranslatable-->\n"


def parse_exchange(param: any) -> str:
    """
    Parses parameter to check if is an exchange parameter value and returns the
    corresponding exchange value in the pt-br format.

    Parameters:
        param (any): The parameter value to be parsed.

    Returns:
        str: The exchange value with the corresponding exchange.
    """
    param = str(param).lower()
    if "gemw" in param:
        return "gemw\n"
    elif "no" in param:
        return "Não\n"
    else:
        parsed = str(param).replace("\n", "")
        return f" {parsed} <!--Untranslatable-->\n"


def parse_actions(param: any) -> str:
    """
    Parses parameter values to get all the actions listed and tries to find the
    corresponding action in the pt-br actions list relation list.

    Parameters:
        param (any): The parameters values to be parsed.

    Returns:
        str: The corresponding actions in pt-br.
    """
    param = str(param).lower()
    params = [x.replace(",", "") for x in param.replace("\n", "").split(",") if x != ""]
    params = [x.rstrip().lstrip() for x in params]
    actions_list = get_actions_lists()
    lowered_actions = [x.lower() for x in actions_list[0]]
    actions = []
    for p in params:
        if p in lowered_actions:
            idx = lowered_actions.index(p)
            actions.append(actions_list[1][idx])
        else:
            actions.append(f"{p} <!--Unrecognized action-->")
    return ", ".join(actions) + "\n"
