# -*- coding: utf-8 -*-
"""
Infoboxes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""

from .classes import InfoboxParameters
from .functions import get_template_by_name, retrieve_parameters
from .general import jsons_path

# Defines the Infobox Item
InfoboxItem = InfoboxParameters(
    "Infobox objeto", "Infobox Item", jsons_path + "item.json"
)

# Defines the Infobox Monster
InfoboxMonster = InfoboxParameters(
    "Infobox Monstro", "Infobox Monster new", jsons_path + "monster.json"
)


# Defines the Infobox Familiar
InfoboxFamiliar = InfoboxParameters(
    "Infobox Familiar", "Infobox Familiar", jsons_path + "familiar.json"
)


from .parsers import (
    parse_actions,
    parse_date,
    parse_destroy,
    parse_disassembly,
    parse_exchange,
    parse_float,
    parse_int,
    parse_int_or_float,
    parse_item_name,
    parse_kept,
    parse_lfpoints,
    parse_name_english,
    parse_poisonous,
    parse_primarystyle,
    parse_quest,
    parse_restriction,
    parse_speed,
    parse_style,
    parse_yes_no,
)


def translate_infobox_item(t):
    def parser(param, param_val, name=None, num=0):
        if "None" in param_val:
            param_val = param_val.replace(" ", "").replace("None", " Nenhum")
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
            print("> Failed to parse the parameter: ", param)
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
                print(f"> Unable to retrieve {e} parameter.")

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
    print("Trying to find Infobox Item...")
    try:
        t = get_template_by_name(page, InfoboxItem.en)
        print("Infobox Item found and translated.\n" + 50 * "-")
        return translate_infobox_item(t)
    except:
        raise Exception(
            "> Error while parsing Infobox Item.\nProbably the template is not in the page."
        )


def translate_infobox_monster(t):
    def parser(param, param_val, name=None, num=0):
        if "None" in param_val:
            param_val = param_val.replace(" ", "").replace("None", " Nenhum")
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
                elif param == "name":
                    parsed = parse_name_english(param_val, num)
                else:
                    parsed = str(param_val).replace("\n", "")
                    parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("> Failed to parse the parameter: ", param)
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
                print(f"> Unable to retrieve {e} parameter.")

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
    print("Trying to find Infobox Monster...")
    try:
        t = get_template_by_name(page, InfoboxMonster.en)
        print("Infobox Monster found and translated.\n" + 50 * "-")
        return translate_infobox_monster(t)
    except:
        raise Exception(
            "> Error while parsing Infobox Monster.\nProbably the template is not in the page."
        )


def translate_infobox_familiar(t):
    def parser(param, param_val, name=None, num=0):
        if "None" in param_val:
            param_val = param_val.replace(" ", "").replace("None", " Nenhum")
        try:
            if param == "name":
                parsed = parse_name_english(param_val, num)
            elif param in [
                "id",
                "level",
                "attack",
                "defence",
                "magic",
                "ranged",
                "max",
                "lifepoints",
                "points",
                "time",
                "combat",
            ]:
                parsed = parse_int(param_val)
            elif param == "immune to poison":
                parsed = parse_yes_no(param_val)
            elif param == "style":
                parsed = parse_primarystyle(param_val)
            elif param == "release":
                parsed = parse_date(param_val)
            elif param == "size":
                parsed = str(param_val)
            else:
                parsed = str(param_val).replace("\n", "")
                parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("> Failed to parse the parameter: ", param)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        if int(num) > 0:
            return f"|{InfoboxFamiliar.get_parameter(param).br}{num} = {parsed}"
        else:
            return f"|{InfoboxFamiliar.get_parameter(param).br} = {parsed}"

    def parse_all(t):
        parameters = retrieve_parameters(t)
        output = f"{{{{{InfoboxFamiliar.br}\n"

        for param in parameters:
            try:
                if int(param[1]) > 0:
                    param_val = t.get(param[0] + param[1]).value
                    output += parser(param[0], param_val, num=param[1])
                else:
                    param_val = t.get(param[0]).value
                    output += parser(param[0], param_val, num=param[1])
            except Exception as e:
                print(param, param_val)
                print(f"> Unable to retrieve {e} parameter.")

        output += f"}}}}"
        return output

    return parse_all(t)


def get_infobox_familiar(page) -> str:
    """
    Returns the translated Infobox Familiar.

    Parameters:
        page: The page to search the Infobox Familiar.

    Returns:
        str: The Infobox Familiar.
    """
    print("Trying to find Infobox Familiar...")
    try:
        t = get_template_by_name(page, InfoboxFamiliar.en)
        output = translate_infobox_familiar(t)
    except AttributeError:
        t = get_template_by_name(page, "Infobox familiar")
        output = translate_infobox_familiar(t)
    except:
        raise Exception(
            "> Error while parsing Infobox Familiar!\nProbably the template is not in the page."
        )

    print("Infobox Familiar found and translated.\n" + 50 * "-")
    return output
