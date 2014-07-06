__author__ = 'alex'
# -*- coding: utf-8 -*-

import json
from mptt.templatetags.mptt_tags import cache_tree_children
from tree_to_xml.src.main.models import Structure


def create_node(parent_id, name, node_type):
    result = {
        "error": 0
    }

    try:
        parent = Structure.objects.get(pk=parent_id)
    except Exception:
        result["error"] = 1

    try:
        new_node = Structure.objects.create(name=name, type=node_type, parent=parent)
    except Exception as e:
        result["error"] = 2
        result["message"] = e

    result["id"] = new_node.pk
    return result


def update_name(node_id, name):
    result = {
        "error": 0
    }

    try:
        node = Structure.objects.get(pk=node_id)
    except Exception as e:
        result["error"] = 3
        result["message"] = e
        return result

    node.name = name
    node.save()
    result["id"] = node.pk
    return result


def delete_node(node_id):
    result = {
        "error": 0
    }

    try:
        node = Structure.objects.get(pk=node_id)
    except Exception as e:
        result["error"] = 3
        result["message"] = e
        return result
    node.delete()
    return result


def get_all_json_struct():
    def recursive_node_to_dict(node):
        result = {
            'id': node.pk,
            'text': node.name,
            'type': node.type,
        }
        children = [recursive_node_to_dict(c) for c in node.get_children()]
        if children:
            result['children'] = children
        return result

    root_nodes = cache_tree_children(Structure.objects.all())
    dicts = []
    for n in root_nodes:
        dicts.append(recursive_node_to_dict(n))

    return dicts