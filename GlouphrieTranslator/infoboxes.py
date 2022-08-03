# -*- coding: utf-8 -*-
"""
Infoboxes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""

from curses.ascii import isdigit
from .classes import InfoboxParameters
from .general import jsons_path, get_item_br_name_by_en

# Defines the Infobox Item
InfoboxItem = InfoboxParameters(
    "Infobox objeto", 
    "Infobox Item", 
    jsons_path + "item.json"
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
    parse_version,
    parse_kept,
    parse_quest,
    parse_restriction,
    parse_yes_no,
    parse_exchange,
)


def translate_infobox_items(t):
    def parser(param, param_val, id=None, name=None, num=0):
        def verify_multiple(param_en, lst):
            """Checks if the given english param matches one of multiple."""
            for item in lst:
                if param_en in item:
                    return True
            return False

        try:
            if "name" in param.en:
                return parse_item_name(param_val, num)
            elif "version" in param.en:
                parsed = parse_version(param_val)
            elif "weight" in param.en:
                parsed = parse_float(param_val)
            elif "quest" in param.en:
                parsed = parse_quest(param_val)
            elif "disassembly" in param.en:
                parsed = parse_disassembly(param_val)
            elif "value" in param.en:
                parsed = parse_int(param_val)
            elif "exchange" in param.en:
                parsed = parse_exchange(param_val)
            elif "id" in param.en:
                if isinstance(param_val, list):
                    parsed = [parse_int(x) for x in param_val]
                    parsed = ", ".join(parsed)
                else:
                    parsed = parse_int(param_val)
            elif verify_multiple(param.en, ["release", "removal"]):
                parsed = parse_date(param_val)
            elif "examine" in param.en:
                parsed = parse_examine(param_val, id, name)
            elif "kept" in param.en:
                parsed = parse_kept(param_val)
            elif "restriction" in param.en:
                parsed = parse_restriction(param_val)
            elif "destroy" in param.en:
                parsed = parse_destroy(param_val)
            elif verify_multiple(param.en, [
                "actions",
                "actions_ground",
                "actions_equipped",
                "actions_bank",
                "actions_currency_pouch",
            ]):
                parsed = parse_actions(param_val)
            elif verify_multiple(param.en, [
                "stacksinbank",
                "stackable",
                "equipable",
                "tradeable",
                "members",
                "alchable",
            ]):
                parsed = parse_yes_no(param_val)
            else:
                parsed = str(param_val).replace("\n", "")
                parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("Failed to parse the parameter: ", param.en)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        if num == 0:
            return f"|{param.br} = {parsed}"
        else:
            return f"|{param.br}{num} = {parsed}"

    def simple_item(t):
        output = f"{{{{{InfoboxItem.br}\n"

        for param in InfoboxItem.parameters:
            try:
                # Kinda ugly, but hey — gets the job done.
                if param.en == "examine":
                    id = int(str(t.get("id").value)) # Cheeky way of getting rid of unwanted spaces.
                    name = str(t.get("name").value)
                    name = " ".join([x for x in name.replace("\n", "").split(" ") if x != ""])
                    name = get_item_br_name_by_en(name).replace(" ", "_")
                    param_val = t.get(param.en).value
                    output += parser(param, param_val, id, name)
                else:
                    param_val = t.get(param.en).value
                    output += parser(param, param_val)
            except Exception as e:
                print(f"Unable to retrieve {e} parameter.")

        output += f"}}}}"
        return output

    def complex_item(t):
        output = f"{{{{{InfoboxItem.br}\n"
        number = ""

        for param in InfoboxItem.parameters:
            # Needs to loop 4 times (instead of only 3) because sometimes
            # there's the generic param and only the odd one out has a number,
            # for example 'examine' and then only 'examine3' because 1 and 2 are the same.
            for i in range(4):
                try:
                    # Makes so that it goes 'example', 'example1', 'example2' and 'example3'.
                    number = "" if i == 0 else str(i)

                    if param.en == "examine":
                        try:
                            id = int(str(t.get("id" + number).value))
                        except ValueError:
                            id = int(str(t.get("id1").value)) # Assuming 'id1' exists when 'id' doesnt.

                        try:
                            name = str(t.get("name" + number).value)
                        except ValueError:
                            name = str(t.get("name1").value) # Assuming 'name1' exists when 'name' doesnt.
                        name = " ".join([x for x in name.replace("\n", "").split(" ") if x != ""])
                        name = get_item_br_name_by_en(name).replace(" ", "_")

                        try:
                            param_val = t.get("examine" + number).value
                        except ValueError:
                            param_val = t.get("examine" + "1").value # Assuming 'examine1' exists when 'examine' doesnt.

                        output += parser(param, param_val, id, name, i)
                    else:
                        param_val = t.get(param.en + number).value
                        output += parser(param, param_val, num = i)
                except Exception:
                    pass # Cba to spam all the unparsed params here.

        output += f"}}}}"
        return output

    num_of_params = len(t.split("\n"))
    if num_of_params < 30:    
        return simple_item(t)
    else:
        return complex_item(t)