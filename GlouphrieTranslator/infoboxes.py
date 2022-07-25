# -*- coding: utf-8 -*-
"""
Infoboxes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""

from .classes import InfoboxParameters
from .general import jsons_path, get_item_br_name_by_en

# Defines the Infobox Item
InfoboxItem = InfoboxParameters(
    "Infobox objeto", "Infobox Item", jsons_path + "item.json"
)

from .parsers import (
    parse_actions,
    parse_date,
    parse_examine,
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


def translate_infobox_items(t):
    def parser(param, param_val, id=None, name=None):
        try:
            if param.en == "name":
                return parse_item_name(param_val)
            elif param.en == "weight":
                parsed = parse_float(param_val)
            elif param.en == "quest":
                parsed = parse_quest(param_val)
            elif param.en == "disassembly":
                parsed = parse_disassembly(param_val)
            elif param.en in ["value"]:
                parsed = parse_int(param_val)
            elif param.en == "exchange":
                parsed = parse_exchange(param_val)
            elif param.en == "id":
                if isinstance(param_val, list):
                    parsed = [parse_int(x) for x in param_val]
                    parsed = ", ".join(parsed)
                else:
                    parsed = parse_int(param_val)
            elif param.en in ["release", "removal"]:
                parsed = parse_date(param_val)
            elif param.en in "examine":
                parsed = parse_examine(param_val, id, name)
            elif param.en == "kept":
                parsed = parse_kept(param_val)
            elif param.en == "restriction":
                parsed = parse_restriction(param_val)
            elif param.en == "destroy":
                parsed = parse_destroy(param_val)
            elif param.en in [
                "actions",
                "actions_ground",
                "actions_equipped",
                "actions_bank",
                "actions_currency_pouch",
            ]:
                parsed = parse_actions(param_val)
            elif param.en in [
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
            print("Failed to parse the parameter: ", param.en)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        return f"|{param.br} = {parsed}"

    output = f"{{{{{InfoboxItem.br}\n"

    for param in InfoboxItem.parameters:
        try:
            # Kinda ugly, but hey — gets the job done.
            if param.en == "examine":
                id = int(
                    str(t.get("id").value)
                )  # Cheeky way of getting rid of unwanted spaces.
                name = str(t.get("name").value)
                name = " ".join(
                    [x for x in name.replace("\n", "").split(" ") if x != ""]
                )
                # 'parse_item_name()' returns more than only the name, thus can't be used.
                name = get_item_br_name_by_en(name).replace(" ", "_")
                param_val = t.get(param.en).value
                output += parser(param, param_val, id, name)
            else:
                param_val = t.get(param.en).value
                output += parser(param, param_val)
        except Exception as e:
            print(f"Unable to retrieve '{e}' parameter.")

    output += f"}}}}"
    return output
