# -*- coding: utf-8 -*-
"""
General stuff file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
from os.path import abspath, dirname
import json

jsons_path = abspath(dirname(__file__)) + "\\jsons\\"


# TODO: Put in an overall json file with common stuff.
months_br = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]
months_en = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def get_items_list():
    """
    Returns a list of all items in the game, with their pt-br and english names.

    Returns:
        list: A list of all items in the game, with their pt-br and english name.
    """
    names = open(abspath(dirname(__file__)) + "\\jsons\\item_names_pt_en.json")
    names = json.load(names)
    return names



def get_actions_lists():
    """
    Returns:
        list: A list of all actions in english and pt-br.
    """
    with open(jsons_path + "actions_list.json", "r", encoding="utf-8") as json_file:
        actions = json.load(json_file)
        json_file.close()
    return [list(actions.keys()), list(actions.values())]


def get_item_names_by_id(id: int) -> list:
    """
    Returns the br and english names of an item by its id.

    Parameters:
        id (int): The id of the item.

    Returns:
        list: A list with the br and english names of the item.
    """
    items_list = get_items_list()
    try:
        for item in items_list:
            if int(item[0]) == id:
                return item[1], item[2]
    except:
        return None


def get_item_br_name_alias(en_name: str) -> str:
    """
    Returns the pt-br name of an item by its english name.

    Parameters:
        en_name (str): The english name of the item.

    Returns:
        str: The pt-br name of the item.
    """
    items_list = get_items_list()
    try:
        index = 0
        for item in items_list:
            if en_name in item:
                break
            index += 1
        return items_list[index][1]
    except:
        return None


def get_item_en_name_alias(br_name: str) -> str:
    """
    Returns the english name of an item by its pt-br name.

    Parameters:
        br_name (str): The pt-br name of the item.

    Returns:
        str: The english name of the item.
    """
    items_list = get_items_list()
    try:
        index = 0
        for item in items_list:
            if br_name in item:
                break
            index += 1
        return items_list[index][2]
    except:
        return None
