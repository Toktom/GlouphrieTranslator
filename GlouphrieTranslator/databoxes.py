# -*- coding: utf-8 -*-
"""
Infoboxes file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""

from .classes import InfoboxParameters
from .functions import get_template_by_name, retrieve_parameters
from .general import jsons_path

# Defines the Databox Summoning Pouch
DataboxSummoningPouch = InfoboxParameters(
    "Databox Algibeiras de Evocação",
    "Databox Summoning pouch",
    jsons_path + "summoning_pouch.json",
)

# Defines the Databox Summoning Scroll
DataboxSummoningScroll = InfoboxParameters(
    "Databox Pergaminhos de Evocação",
    "Databox Summoning scroll",
    jsons_path + "summoning_scroll.json",
)

from .parsers import (
    parse_charm,
    parse_exchange,
    parse_float,
    parse_int,
    parse_int_or_float,
)


def translate_databox_summoning_pouch(t):
    def parser(param, param_val, name=None, num=0):
        try:
            if param in ["shards", "returnlvl"]:
                parsed = parse_int(param_val)
            elif param in ["low", "high"]:
                parsed = parse_int_or_float(param_val, longfloat=True)
            elif param in ["createxp", "usexp"]:
                parsed = parse_float(param_val)
            elif param == "exchange":
                parsed = parse_exchange(param_val)
            elif param == "charm":
                parsed = parse_charm(param_val)
            else:
                parsed = str(param_val).replace("\n", "")
                parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("> Failed to parse the parameter: ", param)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        if int(num) > 0:
            return f"|{DataboxSummoningPouch.get_parameter(param).br}{num} = {parsed}"
        else:
            return f"|{DataboxSummoningPouch.get_parameter(param).br} = {parsed}"

    def parse_all(t):
        parameters = retrieve_parameters(t)
        output = f"{{{{{DataboxSummoningPouch.br}\n"

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


def get_databox_summoning_pouch(page) -> str:
    """
    Returns the translated Databox Summoning Pouch.

    Parameters:
        page: The page to search the Databox Summoning Pouch.

    Returns:
        str: The Databox Summoning Pouch.
    """
    print("Trying to find Databox Summoning Pouch...")
    try:
        t = get_template_by_name(page, DataboxSummoningPouch.en)
        output = translate_databox_summoning_pouch(t)
    except AttributeError:
        t = get_template_by_name(page, "Infobar Summon Pouch")
        output = translate_databox_summoning_pouch(t)
    except:
        raise Exception(
            "> Error while parsing Databox Summoning Pouch!\nProbably the page doesn't have a Databox Summoning Pouch."
        )

    print("Databox Summoning Pouch found and translated.\n" + 50 * "-")
    return output


def translate_databox_summoning_scroll(t):
    def parser(param, param_val, name=None, num=0):
        try:
            if param in ["special", "returnlvl"]:
                parsed = parse_int(param_val)
            elif param in ["low", "high"]:
                parsed = parse_int_or_float(param_val, longfloat=True)
            elif param == "exchange":
                parsed = parse_exchange(param_val)
            elif param in ["createxp", "usexp"]:
                parsed = parse_float(param_val)
            else:
                parsed = str(param_val).replace("\n", "")
                parsed = f"{parsed} <!--Untranslatable-->\n"
        except Exception as e:
            print("> Failed to parse the parameter: ", param)
            parsed = str(param_val).replace("\n", "")
            parsed = f"{parsed} <!--Failed-->\n"

        if int(num) > 0:
            return f"|{DataboxSummoningScroll.get_parameter(param).br}{num} = {parsed}"
        else:
            return f"|{DataboxSummoningScroll.get_parameter(param).br} = {parsed}"

    def parse_all(t):
        parameters = retrieve_parameters(t)
        output = f"{{{{{DataboxSummoningScroll.br}\n"

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


def get_databox_summoning_scroll(page) -> str:
    """
    Returns the translated Databox Summoning Scroll.

    Parameters:
        page: The page to search the Databox Summoning Scroll.

    Returns:
        str: The Databox Summoning Scroll.
    """
    print("Trying to find Databox Summoning Scroll...")
    try:
        t = get_template_by_name(page, DataboxSummoningScroll.en)
        output = translate_databox_summoning_scroll(t)
    except AttributeError:
        t = get_template_by_name(page, "Infobar Summon Scroll")
        output = translate_databox_summoning_scroll(t)
    except:
        raise Exception(
            "> Error while parsing Databox Summoning Scroll!\nProbably the page doesn't have a Databox Summoning Scroll."
        )

    print("Databox Summoning Scroll found and translated.\n" + 50 * "-")
    return output
