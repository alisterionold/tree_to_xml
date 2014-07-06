__author__ = 'alex'
# -*- coding: utf-8 -*-

from functools import update_wrapper
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse



def render_to_json(func):
    def wrapper(request, *args, **kwargs):
        result = func(request, *args, **kwargs)
        json_data = json.dumps(result, cls=DjangoJSONEncoder)
        return HttpResponse(json_data, mimetype="application/json")
    return update_wrapper(wrapper, func)


def render_to_xml(func):
    def wrapper(request, *args, **kwargs):
        result = func(request, *args, **kwargs)
        response = HttpResponse(result, mimetype='text/xml')
        response['Content-Disposition'] = 'attachment; filename=tree_structure.xml'
        response['Content-Length'] = len(result)
        return response
    return update_wrapper(wrapper, func)