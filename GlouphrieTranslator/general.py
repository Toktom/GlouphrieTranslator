# -*- coding: utf-8 -*-
"""
General stuff file
=================
@Author: Michael Markus Ackermann (a.k.a. Toktom)
"""
from os.path import abspath, dirname
import json

jsons_path = abspath(dirname(__file__)) + "\\jsons\\"

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
    with open(
        abspath(dirname(__file__)) + "\\txts\\items_list.txt", "r", encoding="utf-8"
    ) as f:
        lines = f.readlines()
        f.close()
    lines = lines[2:]
    lines = [x.replace("\n", "") for x in lines]
    lines = [x.split("\t") for x in lines]
    lines = [x for x in lines if not "NO_PT_NAME" in x]
    lines = [x for x in lines if not "P/h" in x]
    lines = [[y for y in x if y != ""] for x in lines]
    return lines


def get_actions_lists():
    with open(jsons_path + "actions_list.json", "r", encoding="utf-8") as json_file:
        actions = json.load(json_file)
        json_file.close()
    return [list(actions.keys()), list(actions.values())]


def get_item_names_by_id(id):
    items_list = get_items_list()
    try:
        for item in items_list:
            if int(item[0]) == id:
                return (item[1], item[2])
    except:
        return None


def get_item_br_name_alias(en_name):
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


def get_item_en_name_alias(br_name):
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
