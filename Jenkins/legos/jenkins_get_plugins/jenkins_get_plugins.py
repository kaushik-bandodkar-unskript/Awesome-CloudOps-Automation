##
##  Copyright (c) 2021 unSkript, Inc
##  All rights reserved.
##
from pydantic import BaseModel
from typing import  List
import pprint


class InputSchema(BaseModel):
    pass

def jenkins_get_plugins_printer(output):
    if output is None:
        return
    pprint.pprint(output)

def jenkins_get_plugins(handle) -> List:
    """jenkins_get_plugins returns the jenkins plugins list.

        :rtype: List with jenkins plugins.
    """
    res = []
    plugins = handle.get_plugins().keys()
    for plugin in plugins:
        res.append(plugin)
    return res
