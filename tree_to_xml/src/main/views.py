__author__ = 'alex'
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from tree_to_xml.src.main.models import Structure
from tree_to_xml.src.main.utils import *
from tree_to_xml.src.main.actions import *


def index(request):
    try:
        Structure.objects.get(name="Root")
    except Exception:
        Structure.objects.create(name="Root")

    return render_to_response("main/index.html")


@render_to_json
def get_all(request):
    return get_all_json_struct()


@render_to_json
def create(request):
    parent_id = request.POST.get("parent_id", 0)
    name = request.POST.get("name", None)
    node_type = request.POST.get("type", None)
    return create_node(parent_id, name, node_type)


@render_to_json
def update(request):
    node_id = request.POST.get("id", 0)
    name = request.POST.get("text", None)
    return update_name(node_id, name)

@render_to_json
def delete(request):
    node_id = request.POST.get("id", 0)
    return delete_node(node_id)

@render_to_xml
def get_xml(request):
    from dicttoxml import dicttoxml
    xml = dicttoxml(get_all_json_struct())
    return xml