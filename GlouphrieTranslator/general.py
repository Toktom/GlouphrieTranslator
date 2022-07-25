# -*- coding: utf-8 -*-
"""
General stuff file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
@Coauthor: João Pedro Droval (a.k.a. PvM Dragonic)
"""
from os.path import abspath, dirname
import json

jsons_path = abspath(dirname(__file__)) + "\\jsons\\"


def get_items_list():
    """
    Returns:
        list: A list of all items in the game, with their pt-br and english name.
    """
    names = open(jsons_path + "item_names_pt_en.json")
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
    Parameters:
        id (int): The id of the item.

    Returns:
        tuple: A tuple with the pt-br and english names of the given id.
    """
    items_list = get_items_list()
    try:
        for item in items_list:
            if item[0] == id:
                return item[1], item[2]
    except:
        return None


def get_item_br_name_by_en(en_name: str) -> str:
    """
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


def get_item_en_name_by_br(br_name: str) -> str:
    """
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
