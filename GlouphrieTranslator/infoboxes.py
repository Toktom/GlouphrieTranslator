# -*- coding: utf-8 -*-
"""
Infoboxes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""

from .classes import InfoboxParameters
from .functions import retrieve_parameters, get_template_by_name
from .general import jsons_path

# Defines the Infobox Item
InfoboxItem = InfoboxParameters(
    "Infobox objeto", "Infobox Item", jsons_path + "item.json"
)

# Defines the Infobox Monster
InfoboxMonster = InfoboxParameters(
    "Infobox Monstro", "Infobox Monster new", jsons_path + "monster.json"
)


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
    parse_speed,
    parse_primarystyle,
    parse_style,
    parse_poisonous,
    parse_lfpoints,
    parse_int_or_float,
)


def translate_infobox_item(t):
    def parser(param, param_val, name=None, num=0):
        try:
            if param == "name":
                return parse_item_name(param_val, num)
            elif param == "weight":
                parsed = parse_float(param_val)
            elif param == "quest":
                parsed = parse_quest(param_val)
            elif param == "disassembly":
                parsed = parse_disassembly(param_val)
            elif param in ["value"]:
                parsed = parse_int(param_val)
            elif param == "exchange":
                parsed = parse_exchange(param_val)
            elif param == "id":
                parsed = parse_int(param_val)
            elif param in ["release", "removal"]:
                parsed = parse_date(param_val)
            elif param == "kept":
                parsed = parse_kept(param_val)
            elif param == "restriction":
                parsed = parse_restriction(param_val)
            elif param == "destroy":
                parsed = parse_destroy(param_val)
            elif param in [
                "actions",
                "actions_ground",
                "actions_equipped",
                "actions_bank",
                "actions_currency_pouch",
            ]:
                parsed = parse_actions(param_val)
            elif param in [
                "stacksinbank",
                "stackable",
                "equipable",
                "tradeable",
                "members",
                "alchable",
            ]:
                parsed = parse_yes_no(param_val)
            else:
                parsed = str(param_val).replace("\n", "")
                parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("Failed to parse the parameter: ", param)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        if param != "image":
            if int(num) > 0:
                return f"|{InfoboxItem.get_parameter(param).br}{num} = {parsed}"
            else:
                return f"|{InfoboxItem.get_parameter(param).br} = {parsed}"

    def parse_all(t):
        parameters = retrieve_parameters(t)
        output = f"{{{{{InfoboxItem.br}\n"

        for param in parameters:
            try:
                if param[0] not in ["image", "noteable", "ikod", "store", "lendable"]:
                    if int(param[1]) > 0:
                        param_val = t.get(param[0] + param[1]).value
                        output += parser(param[0], param_val, num=param[1])
                    else:
                        param_val = t.get(param[0]).value
                        output += parser(param[0], param_val, num=param[1])
            except Exception as e:
                print(param, param_val)
                print(f"Unable to retrieve {e} parameter.")

        output += f"}}}}"
        return output

    return parse_all(t)


def get_infobox_item(page) -> str:
    """
    Returns the translated Infobox Item.

    Parameters:
        page: The page to search the Infobox Item.

    Returns:
        str: The Infobox Item.
    """
    try:
        t = get_template_by_name(page, InfoboxItem.en)
        print("Infobox Item found and translated.")
        return translate_infobox_item(t)
    except:
        raise Exception("Error while parsing Infobox Item!")


def translate_infobox_monster(t):
    def parser(param, param_val, name=None, num=0):
        try:
            if "$" in param_val:
                parsed = str(param_val).replace("\n", "")
                parsed = f"{parsed} <!--Skipped-->\n"
            else:
                if param in [
                    "members",
                    "aggressive",
                    "immune_to_poison",
                    "immune_to_deflect",
                    "immune_to_stun",
                    "immune_to_drain",
                    "voice",
                ]:
                    parsed = parse_yes_no(param_val)
                elif param in [
                    "level",
                    "slaylvl",
                    "attack",
                    "defence",
                    "magic",
                    "ranged",
                    "aff_weakness",
                    "aff_melee",
                    "aff_ranged",
                    "aff_magic",
                    "thieve_lvl",
                ]:
                    parsed = parse_int(param_val)
                elif param in [
                    "acc_melee",
                    "acc_ranged",
                    "acc_magic",
                    "max_spec",
                    "max_melee",
                    "max_magic",
                    "max_ranged",
                    "armour",
                ]:
                    parsed = parse_float(param_val)
                elif param in ["slayxp", "experience"]:
                    parsed = parse_int_or_float(param_val)
                elif param == "lifepoints":
                    parsed = parse_lfpoints(param_val)
                elif param == "poisonous":
                    parsed = parse_poisonous(param_val)
                elif param == "style":
                    parsed = parse_style(param_val)
                elif param == "primarystyle":
                    parsed = parse_primarystyle(param_val)
                elif param == "actions":
                    parsed = parse_actions(param_val)
                elif param == "speed":
                    parsed = parse_speed(param_val)
                elif param == "id":
                    parsed = parse_int(param_val)
                elif param in ["release", "removal"]:
                    parsed = parse_date(param_val)
                elif param == "restriction":
                    parsed = parse_restriction(param_val)
                else:
                    parsed = str(param_val).replace("\n", "")
                    parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("Failed to parse the parameter: ", param)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        if int(num) > 0:
            return f"|{InfoboxMonster.get_parameter(param).br}{num} = {parsed}"
        else:
            return f"|{InfoboxMonster.get_parameter(param).br} = {parsed}"

    def parse_all(t):
        parameters = retrieve_parameters(t)
        output = f"{{{{{InfoboxMonster.br}\n"

        for param in parameters:
            try:
                if not param[0] in ["dropversion"]:
                    if int(param[1]) > 0:
                        param_val = t.get(param[0] + param[1]).value
                        output += parser(param[0], param_val, num=param[1])
                    else:
                        param_val = t.get(param[0]).value
                        output += parser(param[0], param_val, num=param[1])
            except Exception as e:
                print(param, param_val)
                print(f"Unable to retrieve {e} parameter.")

        output += f"}}}}"
        return output

    return parse_all(t)


def get_infobox_monster(page) -> str:
    """
    Returns the translated Infobox Monster.

    Parameters:
        page: The page to search the Infobox Monster.

    Returns:
        str: The Infobox Monster.
    """
    try:
        t = get_template_by_name(page, InfoboxMonster.en)
        print("Infobox Monster found and translated.")
        return translate_infobox_monster(t)
    except:
        raise Exception("Error while parsing Infobox Monster!")
